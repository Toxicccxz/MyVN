# Development Workflow

## Working model

Keep `main` stable and use a focused branch for a coherent feature, chapter slice, fix, or engine upgrade. The process is disciplined but lightweight:

```text
stable main
  -> create focused branch
  -> implement small slices
  -> lint frequently
  -> run targeted tests
  -> runtime-check player-visible changes
  -> review diff
  -> update durable docs if project truth changed
  -> create PR when ready if using PR workflow
  -> merge only with user authorization
```

Useful branch names include:

```text
feature/prologue-vertical-slice
feature/ch01-apartment
feature/custom-choice-ui
feature/gallery
fix/save-regression
fix/missing-sprite
chore/renpy-upgrade
```

Do not add enterprise-style phase or audit ceremony to ordinary scene work. One coherent milestone may use one branch; avoid a branch for every tiny scene.

## Local commands

Set `RENPY_SDK` to a Ren'Py 8.5.3 SDK root, then run:

```powershell
.\tools\run.ps1
.\tools\lint.ps1
.\tools\test.ps1
```

Lint every meaningful `.rpy` change. Run targeted testcases for durable or regression-prone paths and runtime-check player-visible changes. Review the final diff and report only checks actually performed. Lint is not a visual check.

## Commits and external actions

Prefer focused commits such as:

```text
feat: add prologue door choice
feat: add Lin character sprite states
test: cover prologue branch convergence
fix: initialize trust state for old saves
docs: update chapter 1 canon
```

Do not force-push, merge, publish, upload a release, or modify remote/security settings without explicit authorization. A runnable local build is not automatically a public release.

## Durable document updates

- Update `STORY_BIBLE.md` when canonical story, character, continuity, tone, or content-boundary truth changes.
- Update `ARCHITECTURE.md` when stable technical structure or boundaries change, not for incidental implementation detail.
- Update `DEVELOPMENT.md` when the team workflow, tooling, Git practice, or validation contract changes.
- Update `ROADMAP.md` when planned milestones or their high-level scope/status changes.
- Update `STATUS.md` whenever actual project state, known validation, risks, or next action materially changes.
- Append to `DECISIONS.md` only for durable accepted choices future work should not repeatedly reopen.

Engine upgrades are dedicated tasks with explicit compatibility and validation work; never change the SDK incidentally. Ren'Py 8.5.3 remains supported until such a task changes that decision.

