# Chiang Mai Wall Book

This repository develops the Chiang Mai wall book.

## Requirements

Using `wt sync` requires Git, Make, Worktrunk 0.80.0 or newer, and an
authenticated GitHub CLI (`gh`). Install Worktrunk's shell integration once:

```sh
wt config shell install
```

Python 3 and `uv` are required to run the sync behavior tests.

## Syncing worktrees

Run `wt sync` from any worktree. It switches the calling shell to the
repository's `master` worktree, pulls `master`, prunes remote-tracking refs,
then checks for stale branches.

Cleanup is limited to local branches whose upstream is gone, whose configured
remote matches `master`, and whose upstream was the same-named remote branch.
The same-named remote ref must still be absent after pruning. The current
branch tip must exactly match a merged pull request targeting `master`.
Branches that fail those checks remain untouched. Worktrunk removes eligible
clean worktrees in the foreground and deletes a branch only when its own
integration checks allow it. Dirty or locked worktrees stay registered, and
unintegrated branch commits remain available.

## Tests

Run the isolated sync behavior suite with:

```sh
make test-git-sync
```

## CI and releases

CI has exactly two jobs, both required to report on every pull request targeting `master`:

- `Checks` runs the repository's validation, currently `make test-git-sync`
  with a pinned Worktrunk download, then `tofu fmt -check`, `tofu init
  -backend=false` and `tofu validate` on `infra/github` (see
  [`infra/github/README.md`](infra/github/README.md)).
- `Release Projection` validates that the pull request title is a Conventional
  Commit and comments with the release the pull request would cause (often
  none). An invalid title or a projection error fails the job. Release-please's
  own release pull requests keep the title check and skip the projection.

Releases use [release-please](https://github.com/googleapis/release-please) in
manifest mode with one root package and `vX.Y.Z` tags. The first release is
`v0.1.0`. On each push to `master` the `Release Please` workflow opens or
updates a release pull request; merging it writes `CHANGELOG.md`, the tag and
a GitHub release. The workflow authenticates as a GitHub App through the
`RELEASE_BOT_APP_ID` variable and `RELEASE_BOT_PRIVATE_KEY` secret; installing
the App is a manual rollout step.
