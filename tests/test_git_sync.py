"""Protect local work while syncing and cleaning eligible merged branches."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path



REPO = Path(__file__).resolve().parents[1]
BRANCH = "stale"


def run(
    cwd: Path,
    *args: str,
    check: bool = True,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run one command with captured text output in a disposable repository."""
    return subprocess.run(args, cwd=cwd, check=check, capture_output=True, text=True, env=env)


def sandbox(tmp_path: Path) -> dict[str, Path | dict[str, list[dict[str, str]]]]:
    """Create a local bare remote and one merged PR branch with a gone upstream."""
    root = tmp_path
    master = root / "master worktree"
    linked = root / "stale worktree"
    remote = root / "remote.git"
    run(root, "git", "init", "--bare", "--initial-branch=master", str(remote))
    run(root, "git", "init", "--initial-branch=master", str(master))
    (master / ".config").mkdir()
    shutil.copy2(REPO / ".config/wt.toml", master / ".config/wt.toml")
    shutil.copy2(REPO / "Makefile", master / "Makefile")
    (master / "tracked.txt").write_text("master\n", encoding="utf-8")
    run(master, "git", "config", "user.name", "Sync Test")
    run(master, "git", "config", "user.email", "sync@example.invalid")
    run(master, "git", "add", ".config/wt.toml", "Makefile", "tracked.txt")
    run(master, "git", "commit", "-m", "seed")
    run(master, "git", "remote", "add", "origin", str(remote))
    run(master, "git", "push", "-u", "origin", "master")

    run(master, "git", "worktree", "add", "-b", BRANCH, str(linked), "master")
    (linked / "integrated.txt").write_text("merged PR change\n", encoding="utf-8")
    run(linked, "git", "add", "integrated.txt")
    run(linked, "git", "commit", "-m", "integrated branch")
    tip = run(linked, "git", "rev-parse", "HEAD").stdout.strip()
    run(linked, "git", "push", "-u", "origin", BRANCH)
    run(master, "git", "merge", "--ff-only", BRANCH)
    run(master, "git", "push", "origin", "master")
    run(master, "git", "push", "origin", "--delete", BRANCH)

    home = root / "home"
    config_dir = home / ".config" / "worktrunk"
    config_dir.mkdir(parents=True)
    user_config = config_dir / "config.toml"
    user_config.write_text("skip-shell-integration-prompt = true\n", encoding="utf-8")
    system_config = root / "system.toml"
    system_config.touch()
    bin_dir = root / "bin"
    bin_dir.mkdir()
    gh = bin_dir / "gh"
    gh.write_text(
        "#!/usr/bin/env python3\n"
        "import json, os, sys\n"
        "expected = ['pr', 'list', '--state', 'merged', '--head']\n"
        "query = '.[] | select(.baseRefName == \"master\") | .headRefOid'\n"
        "if sys.argv[1:6] != expected or sys.argv[7:11] != ['--limit', '100', '--json', 'headRefOid,baseRefName'] or sys.argv[11:] != ['--jq', query]:\n"
        "    print('unexpected gh invocation', file=sys.stderr); sys.exit(2)\n"
        "branch = sys.argv[6]\n"
        "if branch in os.environ.get('GH_PR_FAIL_BRANCHES', '').split(','):\n"
        "    sys.exit(1)\n"
        "with open(os.environ['GH_PR_DATA'], encoding='utf-8') as stream:\n"
        "    rows = json.load(stream).get(branch, [])\n"
        "for row in rows:\n"
        "    if row['baseRefName'] == 'master': print(row['headRefOid'])\n",
        encoding="utf-8",
    )
    gh.chmod(0o755)
    return {
        "master": master,
        "linked": linked,
        "remote": remote,
        "root": root,
        "gh_data": root / "gh-prs.json",
        "gh_bin": bin_dir,
        "tip": tip,
        "prs": {BRANCH: [{"headRefOid": tip, "baseRefName": "master"}]},
    }


def sync(
    box: dict[str, Path | dict[str, list[dict[str, str]]]],
    cwd: Path | None = None,
    *,
    prs: dict[str, list[dict[str, str]]] | None = None,
    fail_branches: tuple[str, ...] = (),
    env_updates: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run the project alias in an isolated shell and GitHub fixture."""
    root = box["root"]
    assert isinstance(root, Path)
    master = box["master"]
    assert isinstance(master, Path)
    data = box["gh_data"]
    assert isinstance(data, Path)
    gh_bin = box["gh_bin"]
    assert isinstance(gh_bin, Path)
    records = prs if prs is not None else box["prs"]
    assert isinstance(records, dict)
    data.write_text(json.dumps(records), encoding="utf-8")
    env = os.environ.copy()
    for key in tuple(env):
        if key.startswith("WORKTRUNK_"):
            env.pop(key)
    env.update(
        {
            "HOME": str(root / "home"),
            "PATH": f"{gh_bin}:{env['PATH']}",
            "WORKTRUNK_CONFIG_PATH": str(root / "home/.config/worktrunk/config.toml"),
            "WORKTRUNK_SYSTEM_CONFIG_PATH": str(root / "system.toml"),
            "WORKTRUNK_PROJECT_CONFIG_PATH": str(master / ".config/wt.toml"),
            "GH_PR_DATA": str(data),
            "GH_PR_FAIL_BRANCHES": ",".join(fail_branches),
        }
    )
    if env_updates:
        env.update(env_updates)
    caller = cwd or master
    command = 'set -e; source <(command wt config shell init bash); wt -y sync; pwd'
    return run(caller, "bash", "--noprofile", "--norc", "-c", command, check=False, env=env)


def branch_exists(repo: Path, branch: str) -> bool:
    """Check whether a local branch ref still exists."""
    return run(repo, "git", "show-ref", "--verify", f"refs/heads/{branch}", check=False).returncode == 0

def worktree_registered(repo: Path, path: Path) -> bool:
    """Return whether Git still registers the path as a linked worktree."""
    return str(path) in run(repo, "git", "worktree", "list", "--porcelain").stdout



def candidate(
    box: dict[str, Path | dict[str, list[dict[str, str]]]],
    branch: str,
    *,
    linked: bool = False,
) -> tuple[str, Path | None]:
    """Create a pushed local branch, then remove its remote ref to mark it gone."""
    master = box["master"]
    remote = box["remote"]
    root = box["root"]
    assert isinstance(master, Path) and isinstance(remote, Path) and isinstance(root, Path)
    path = root / f"{branch} worktree" if linked else None
    worktree = path or root / f"{branch} temporary worktree"
    run(master, "git", "worktree", "add", "-b", branch, str(worktree), "master")
    (worktree / f"{branch}.txt").write_text(f"{branch}\n", encoding="utf-8")
    run(worktree, "git", "add", f"{branch}.txt")
    run(worktree, "git", "commit", "-m", f"{branch} branch")
    tip = run(worktree, "git", "rev-parse", "HEAD").stdout.strip()
    run(worktree, "git", "push", "-u", "origin", branch)
    if not linked:
        run(master, "git", "worktree", "remove", str(worktree))
    run(master, "git", "push", "origin", "--delete", branch)
    return tip, path


def add_pr(
    box: dict[str, Path | dict[str, list[dict[str, str]]]],
    branch: str,
    tip: str,
    base: str = "master",
) -> dict[str, list[dict[str, str]]]:
    prs = box["prs"]
    assert isinstance(prs, dict)
    prs[branch] = [{"headRefOid": tip, "baseRefName": base}]
    return prs


def test_sync_pulls_prunes_and_switches_calling_shell_from_linked_worktree(tmp_path: Path) -> None:
    """A child process must not leave the caller in its original linked worktree."""
    box = sandbox(tmp_path)
    master, linked, remote, root = (box[key] for key in ("master", "linked", "remote", "root"))
    assert isinstance(master, Path) and isinstance(linked, Path) and isinstance(remote, Path) and isinstance(root, Path)
    caller = root / "caller worktree"
    run(master, "git", "worktree", "add", "-b", "caller", str(caller), "master")
    extra = root / "remote checkout"
    run(root, "git", "clone", str(remote), str(extra))
    run(extra, "git", "config", "user.name", "Sync Test")
    run(extra, "git", "config", "user.email", "sync@example.invalid")
    (extra / "remote-only.txt").write_text("pulled\n", encoding="utf-8")
    run(extra, "git", "add", "remote-only.txt")
    run(extra, "git", "commit", "-m", "remote update")
    run(extra, "git", "push", "origin", "master")
    result = sync(box, caller)

    assert result.returncode == 0, result.stderr
    assert result.stdout.splitlines()[-1] == str(master)
    assert (master / "remote-only.txt").read_text(encoding="utf-8") == "pulled\n"
    assert not linked.exists()
    assert run(master, "git", "show-ref", "--verify", "refs/remotes/origin/stale", check=False).returncode != 0


def test_sync_from_master_finishes_in_master_worktree(tmp_path: Path) -> None:
    """The alias must retain the default worktree when started there."""
    box = sandbox(tmp_path)

    result = sync(box)

    master = box["master"]
    assert isinstance(master, Path)
    assert result.returncode == 0, result.stderr
    assert result.stdout.splitlines()[-1] == str(master)


def test_integrated_exact_pr_tip_removes_worktree_and_branch_before_return(tmp_path: Path) -> None:
    """Gone upstream plus exact merged-PR provenance must offer integrated work to Worktrunk."""
    box = sandbox(tmp_path)

    result = sync(box)

    linked = box["linked"]
    master = box["master"]
    assert isinstance(linked, Path) and isinstance(master, Path)
    assert result.returncode == 0, result.stderr
    assert not linked.exists()
    assert not branch_exists(master, BRANCH)


def test_integrated_branch_without_worktree_is_removed(tmp_path: Path) -> None:
    """An eligible branch-only ref must receive the same Worktrunk integration check."""
    box = sandbox(tmp_path)
    tip, _ = candidate(box, "direct")
    master = box["master"]
    assert isinstance(master, Path)
    run(master, "git", "merge", "--ff-only", "direct")
    run(master, "git", "push", "origin", "master")
    prs = add_pr(box, "direct", tip)

    result = sync(box, prs=prs)

    assert result.returncode == 0, result.stderr
    assert not branch_exists(master, "direct")


def test_gone_upstream_without_matching_pr_preserves_branch_and_worktree(tmp_path: Path) -> None:
    """A deleted remote ref alone must not authorize removal of a linked worktree."""
    box = sandbox(tmp_path)
    result = sync(box, prs={})
    linked, master = box["linked"], box["master"]
    assert isinstance(linked, Path) and isinstance(master, Path)

    assert result.returncode == 0, result.stderr
    assert linked.exists()
    assert branch_exists(master, BRANCH)


def test_branch_without_upstream_is_preserved(tmp_path: Path) -> None:
    """A matching PR SHA must not make an untracked local branch eligible."""
    box = sandbox(tmp_path)
    master = box["master"]
    assert isinstance(master, Path)
    run(master, "git", "branch", "--unset-upstream", BRANCH)
    tip = box["tip"]
    assert isinstance(tip, str)

    result = sync(box, prs=add_pr(box, BRANCH, tip))

    assert result.returncode == 0, result.stderr
    assert branch_exists(master, BRANCH)
    assert box["linked"].exists()


def test_different_remote_upstream_is_preserved(tmp_path: Path) -> None:
    """A gone branch on another remote must not be cleaned as an origin branch."""
    box = sandbox(tmp_path)
    master, root = box["master"], box["root"]
    assert isinstance(master, Path) and isinstance(root, Path)
    other = root / "other.git"
    run(root, "git", "init", "--bare", "--initial-branch=master", str(other))
    run(master, "git", "remote", "add", "backup", str(other))
    run(master, "git", "config", f"branch.{BRANCH}.remote", "backup")
    run(master, "git", "config", f"branch.{BRANCH}.merge", f"refs/heads/{BRANCH}")
    tip = box["tip"]
    assert isinstance(tip, str)

    result = sync(box, prs=add_pr(box, BRANCH, tip))

    assert result.returncode == 0, result.stderr
    assert branch_exists(master, BRANCH)
    assert box["linked"].exists()


def test_differently_named_upstream_is_preserved(tmp_path: Path) -> None:
    """A branch tracking master rather than its own same-named ref has no PR provenance."""
    box = sandbox(tmp_path)
    master = box["master"]
    assert isinstance(master, Path)
    run(master, "git", "branch", f"--set-upstream-to=origin/master", BRANCH)
    tip = box["tip"]
    assert isinstance(tip, str)

    result = sync(box, prs=add_pr(box, BRANCH, tip))

    assert result.returncode == 0, result.stderr
    assert branch_exists(master, BRANCH)
    assert box["linked"].exists()


def test_live_remote_branch_is_preserved(tmp_path: Path) -> None:
    """A still-published branch must not be mistaken for a completed stale branch."""
    box = sandbox(tmp_path)
    master = box["master"]
    assert isinstance(master, Path)
    run(master, "git", "push", "origin", BRANCH)
    tip = box["tip"]
    assert isinstance(tip, str)

    result = sync(box, prs=add_pr(box, BRANCH, tip))

    assert result.returncode == 0, result.stderr
    assert branch_exists(master, BRANCH)
    assert box["linked"].exists()


def test_advanced_branch_tip_does_not_match_merged_pr_tip(tmp_path: Path) -> None:
    """A branch advanced after merge must keep its newer commits and worktree."""
    box = sandbox(tmp_path)
    linked = box["linked"]
    master = box["master"]
    assert isinstance(linked, Path) and isinstance(master, Path)
    old_tip = box["tip"]
    assert isinstance(old_tip, str)
    (linked / "later.txt").write_text("newer work\n", encoding="utf-8")
    run(linked, "git", "add", "later.txt")
    run(linked, "git", "commit", "-m", "later work")

    result = sync(box, prs=add_pr(box, BRANCH, old_tip))

    assert result.returncode == 0, result.stderr
    assert linked.exists()
    assert branch_exists(master, BRANCH)
    assert run(master, "git", "rev-parse", BRANCH).stdout.strip() != old_tip


def test_recreated_branch_without_tracking_provenance_is_preserved(tmp_path: Path) -> None:
    """Reusing a merged SHA without its original upstream must not inherit cleanup authority."""
    box = sandbox(tmp_path)
    master, linked = box["master"], box["linked"]
    assert isinstance(master, Path) and isinstance(linked, Path)
    old_tip = box["tip"]
    assert isinstance(old_tip, str)
    run(master, "git", "worktree", "remove", str(linked))
    run(master, "git", "branch", "-D", BRANCH)
    recreated = "recreated"
    run(master, "git", "branch", recreated, old_tip)
    run(master, "git", "worktree", "add", str(linked), recreated)

    result = sync(box, prs=add_pr(box, recreated, old_tip))

    assert result.returncode == 0, result.stderr
    assert linked.exists()
    assert branch_exists(master, recreated)


def test_failed_github_lookup_preserves_branch_and_warns(tmp_path: Path) -> None:
    """An unavailable PR query must not convert a gone upstream into deletion permission."""
    box = sandbox(tmp_path)
    result = sync(box, fail_branches=(BRANCH,))
    linked, master = box["linked"], box["master"]
    assert isinstance(linked, Path) and isinstance(master, Path)

    assert result.returncode == 0, result.stderr
    assert f"WARN: could not check merged PR for {BRANCH}; kept" in result.stderr
    assert linked.exists()
    assert branch_exists(master, BRANCH)


def test_pr_for_another_base_does_not_authorize_cleanup(tmp_path: Path) -> None:
    """A merged PR targeting another branch must not count as a master merge."""
    box = sandbox(tmp_path)
    tip = box["tip"]
    assert isinstance(tip, str)

    result = sync(box, prs=add_pr(box, BRANCH, tip, base="release"))

    linked, master = box["linked"], box["master"]
    assert isinstance(linked, Path) and isinstance(master, Path)
    assert result.returncode == 0, result.stderr
    assert linked.exists()
    assert branch_exists(master, BRANCH)


def test_matching_unintegrated_pr_tip_removes_only_clean_worktree(tmp_path: Path) -> None:
    """A PR SHA must not force-delete commits when Worktrunk declines integration."""
    box = sandbox(tmp_path)
    tip, linked = candidate(box, "unintegrated", linked=True)
    master = box["master"]
    assert isinstance(master, Path) and linked is not None
    prs = add_pr(box, "unintegrated", tip)

    result = sync(box, prs=prs)

    assert result.returncode == 0, result.stderr
    assert not linked.exists()
    assert branch_exists(master, "unintegrated")
    assert run(master, "git", "cat-file", "-e", "unintegrated:unintegrated.txt", check=False).returncode == 0


def test_dirty_and_untracked_files_survive_refused_removal(tmp_path: Path) -> None:
    """Cleanup must not remove a dirty linked worktree or its untracked user files."""
    box = sandbox(tmp_path)
    linked, master = box["linked"], box["master"]
    assert isinstance(linked, Path) and isinstance(master, Path)
    sentinel = linked / "user-data.txt"
    sentinel.write_text("keep\n", encoding="utf-8")

    result = sync(box)

    assert result.returncode == 0, result.stderr
    assert sentinel.read_text(encoding="utf-8") == "keep\n"
    assert linked.exists()
    assert branch_exists(master, BRANCH)
    assert "could not be removed; kept" in result.stderr
    assert worktree_registered(master, linked)


def test_locked_worktree_is_preserved(tmp_path: Path) -> None:
    """A lock must prevent cleanup even when the branch has a matching merged PR."""
    box = sandbox(tmp_path)
    linked, master = box["linked"], box["master"]
    assert isinstance(linked, Path) and isinstance(master, Path)
    run(master, "git", "worktree", "lock", str(linked))

    result = sync(box)

    assert result.returncode == 0, result.stderr
    assert linked.exists()
    assert worktree_registered(master, linked)
    assert branch_exists(master, BRANCH)


def test_refused_worktree_does_not_block_later_branch_only_cleanup(tmp_path: Path) -> None:
    """A dirty refusal must not prevent later eligible branch-only cleanup."""
    box = sandbox(tmp_path)
    linked, master = box["linked"], box["master"]
    assert isinstance(linked, Path) and isinstance(master, Path)
    sentinel = linked / "untracked.txt"
    sentinel.write_text("keep\n", encoding="utf-8")
    tip, _ = candidate(box, "zz-direct")
    run(master, "git", "merge", "--ff-only", "zz-direct")
    run(master, "git", "push", "origin", "master")
    prs = add_pr(box, "zz-direct", tip)

    result = sync(box, prs=prs)

    assert result.returncode == 0, result.stderr
    assert sentinel.exists()
    assert linked.exists()
    assert branch_exists(master, BRANCH)
    assert worktree_registered(master, linked)
    assert not branch_exists(master, "zz-direct")


def test_pull_failure_stops_before_cleanup(tmp_path: Path) -> None:
    """A failed pull must not let eligible stale work proceed to removal."""
    box = sandbox(tmp_path)
    master, remote = box["master"], box["remote"]
    assert isinstance(master, Path) and isinstance(remote, Path)
    run(master, "git", "remote", "set-url", "origin", str(tmp_path / "missing.git"))

    result = sync(box)

    assert result.returncode != 0
    assert box["linked"].exists()
    assert branch_exists(master, BRANCH)
    assert worktree_registered(master, box["linked"])


def test_fetch_failure_stops_before_cleanup(tmp_path: Path) -> None:
    """A failed prune must not allow cleanup to run against stale ref state."""
    box = sandbox(tmp_path)
    master = box["master"]
    assert isinstance(master, Path)
    real_git = shutil.which("git")
    assert real_git is not None
    shim_dir = tmp_path / "git-shim"
    shim_dir.mkdir()
    shim = shim_dir / "git"
    shim.write_text(
        "#!/bin/sh\n"
        "if [ \"$1\" = fetch ] && [ \"$2\" = --prune ]; then exit 1; fi\n"
        "exec \"$REAL_GIT\" \"$@\"\n",
        encoding="utf-8",
    )
    shim.chmod(0o755)

    gh_bin = box["gh_bin"]
    assert isinstance(gh_bin, Path)
    result = sync(
        box,
        env_updates={
            "PATH": f"{shim_dir}:{gh_bin}:{os.environ['PATH']}",
            "REAL_GIT": real_git,
        },
    )

    assert result.returncode != 0
    assert box["linked"].exists()
    assert branch_exists(master, BRANCH)
