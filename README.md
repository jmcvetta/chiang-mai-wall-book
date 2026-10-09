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
