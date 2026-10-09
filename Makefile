SHELL := /bin/bash
.SHELLFLAGS := -o pipefail -c

.PHONY: __git_sync_run test-git-sync

test-git-sync:
	uv run --no-project --with pytest pytest tests/test_git_sync.py

# Offer only gone, same-remote, same-name upstream branches whose current tip
# exactly matches a merged PR into master. Worktrunk decides whether the
# branch is integrated and whether its worktree is safe to remove.
__git_sync_run:
	git pull
	git fetch --prune
	@remote=$$(git config --get branch.master.remote); \
	if [ -z "$$remote" ]; then \
		printf 'WARN: master has no remote; skipping branch cleanup\n' >&2; \
		exit 0; \
	fi; \
	git branch -vv | awk '/: gone\]/ {sub(/^\+ /, ""); print $$1}' | \
	while read -r branch; do \
		[ "$$branch" = master ] && continue; \
		[ "$$(git config --get "branch.$$branch.remote")" = "$$remote" ] || continue; \
		[ "$$(git config --get "branch.$$branch.merge")" = "refs/heads/$$branch" ] || continue; \
		git show-ref --verify --quiet "refs/remotes/$$remote/$$branch" && continue; \
		tip=$$(git rev-parse --verify "refs/heads/$$branch") || continue; \
		if ! merged=$$(gh pr list --state merged --head "$$branch" --limit 100 \
			--json headRefOid,baseRefName \
			--jq '.[] | select(.baseRefName == "master") | .headRefOid'); then \
			printf 'WARN: could not check merged PR for %s; kept\n' "$$branch" >&2; \
			continue; \
		fi; \
		printf '%s\n' "$$merged" | grep -Fxq "$$tip" || continue; \
		worktree_path=$$(git worktree list --porcelain | awk -v branch="$$branch" \
			'/^worktree / {path = substr($$0, 10)} \
			 /^branch / && substr($$0, 8) == "refs/heads/" branch {print path; exit}'); \
		if [ -n "$$worktree_path" ]; then \
			if ! wt remove --foreground "$$worktree_path"; then \
				printf 'WARN: worktree for merged branch %s could not be removed; kept: %s\n' "$$branch" "$$worktree_path" >&2; \
				continue; \
			fi; \
			printf 'removed merged worktree: %s\n' "$$worktree_path"; \
		elif ! wt remove --foreground "$$branch"; then \
			printf 'WARN: merged branch %s could not be removed; kept\n' "$$branch" >&2; \
		fi; \
	done
