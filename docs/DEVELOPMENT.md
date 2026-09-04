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

## Future real-case research boundary

A documented real homicide case never enters production solely from model memory or a casual suggestion. It requires an explicit case-research task before implementation. That task must:

- Perform explicit research and identify authoritative sources.
- Separate confirmed facts from allegations, disputed accounts, speculation, and reconstruction.
- Record important source provenance.
- Verify names, dates, locations, legal outcomes, and disputed facts.
- Identify whether the matter remains active or legally sensitive.
- Consider the privacy and dignity of surviving relatives.
- Review copyright and licensing for photographs, video, audio, court documents, and news material.
- Avoid presenting disputed theories as established fact; conflicting evidence must be acknowledged.

Codex must never silently invent real-case facts. Research approval does not automatically authorize implementation, and a newly suggested case must not be added without the explicit research step.

## Media provenance

Every case must distinguish authentic archival material, recreated/dramatized material, AI-generated reconstruction, and original game artwork or sound. Maintain case-level source and rights records before release.

AI-generated or recreated imagery must not be presented as authentic crime-scene, police, historical press, or archival evidence. Clearly label reconstruction in context and credits. Do not use recognizable news-brand marks or layouts to imply false authenticity. When evidence provenance is uncertain, omit it or mark the gap rather than guessing.

M1 contains no downloaded third-party media. Its native color panels and text are explicit development placeholders.
