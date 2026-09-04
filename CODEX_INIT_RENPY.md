# Ren'Py Project Foundation Initialization

You are working inside a newly created, clean Ren'Py visual novel project.

Your task is to establish the initial repository architecture, AI-development rules, documentation,
and local Windows tooling for this project.

This task is ONLY the project foundation. Do not write real story content yet.

## First: inspect before editing

Before making changes:

1. Inspect the repository root.
2. Inspect the current `game/` directory and the Ren'Py-generated files.
3. Identify the existing `script.rpy`, `screens.rpy`, `gui.rpy`, `options.rpy`, and any generated assets.
4. Inspect Git status if this is already a Git repository.
5. Do not assume filenames or paths that do not exist.
6. Preserve the clean Ren'Py project's working baseline.

Do not delete or heavily rewrite Ren'Py-generated default files merely to make the project look cleaner.

## Project goal

Build a production-quality visual novel using Ren'Py with a structure that is:

- simple;
- readable;
- safe for long-term Codex-assisted development;
- easy to validate;
- easy to expand chapter by chapter;
- deliberately much lighter than a Godot/RPG architecture.

The project is a visual novel first.

Do NOT create a general-purpose game framework.
Do NOT reproduce Godot-style `core/runtime/presentation/application` layering.
Do NOT add service/repository/controller/domain layers unless a future concrete feature genuinely
requires them.

## Supported engine

The initial supported engine is:

- Ren'Py 8.5.3

Windows is the primary development environment and first development target.

Do not upgrade the engine during this task.

## Core architecture principle

Story and presentation should stay simple; state and reusable behavior should stay explicit.

Use Ren'Py script for:

- narrative flow;
- dialogue;
- narration;
- choices;
- labels;
- scene/image changes;
- transitions;
- ordinary screen behavior;
- normal audio playback.

Use Python only when it clearly reduces duplication or implements genuinely reusable logic.

Prefer built-in Ren'Py functionality over custom replacements.

In particular, preserve Ren'Py's standard:

- save/load;
- rollback;
- history;
- preferences;
- skip;
- auto-forward;
- accessibility;
- standard menu behavior.

Do not implement a custom save system.

## Required root files

Create or update these files:

```text
AGENTS.md
README.md
.editorconfig
.gitignore
docs/ARCHITECTURE.md
docs/DEVELOPMENT.md
docs/STORY_BIBLE.md
docs/ROADMAP.md
docs/STATUS.md
docs/DECISIONS.md
tools/run.ps1
tools/lint.ps1
tools/test.ps1
```

Do not create additional durable policy documents unless clearly necessary.

## Preferred project shape

The intended long-term structure is:

```text
/
├── AGENTS.md
├── README.md
├── .editorconfig
├── .gitignore
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEVELOPMENT.md
│   ├── STORY_BIBLE.md
│   ├── ROADMAP.md
│   ├── STATUS.md
│   └── DECISIONS.md
├── tools/
│   ├── run.ps1
│   ├── lint.ps1
│   └── test.ps1
└── game/
    ├── script.rpy
    ├── options.rpy
    ├── gui.rpy
    ├── screens.rpy
    ├── definitions/
    │   ├── characters.rpy
    │   ├── images.rpy
    │   └── audio.rpy
    ├── state/
    │   ├── variables.rpy
    │   └── helpers.rpy
    ├── story/
    │   ├── prologue/
    │   ├── chapter_01/
    │   ├── chapter_02/
    │   └── endings/
    ├── ui/
    │   ├── screens/
    │   └── styles/
    ├── tests/
    ├── images/
    │   ├── backgrounds/
    │   ├── characters/
    │   ├── cg/
    │   └── ui/
    ├── audio/
    │   ├── bgm/
    │   ├── sfx/
    │   └── voice/
    └── fonts/
```

Important:

This is a target shape, NOT a demand to manufacture empty architecture.

Create directories/files now only when they are useful to the initial foundation.

It is acceptable to create the basic `definitions`, `state`, `story`, `ui`, and `tests` directories
if they make the next development step clearer, but do not populate them with fake production content.

## AGENTS.md requirements

`AGENTS.md` is the main Codex project policy.

It must be detailed enough that future Codex sessions can work safely without repeatedly asking about
basic architecture.

Include the following sections/rules.

### Mission

State that this repository is a Ren'Py visual novel project using Ren'Py 8.5.3.

The project should remain easy to understand, review, and maintain through AI-assisted development.

### Source of truth

Define these ownership rules:

- `docs/STORY_BIBLE.md` owns canonical story/world/character/tone/continuity facts.
- `docs/ARCHITECTURE.md` owns stable technical structure and boundaries.
- `docs/DEVELOPMENT.md` owns development/Git/validation workflow.
- `docs/ROADMAP.md` owns planned milestones.
- `docs/STATUS.md` owns actual current project state.
- `docs/DECISIONS.md` records durable decisions that future work should not repeatedly reopen.
- actual `.rpy` implementation owns actual implemented runtime behavior.

If documentation and implementation conflict, Codex must inspect the context rather than silently
choosing one.

### Story authority

Future Codex tasks must inspect the Story Bible and relevant chapter files before adding important
story facts.

Important canon includes:

- character identity;
- age;
- history;
- relationships;
- motivation;
- personality;
- what each character knows;
- chronology;
- world rules;
- locations;
- route requirements;
- ending conditions;
- established visual traits;
- tone/content boundaries.

Codex must not invent permanent canon when a task does not provide it.

If missing canon is necessary, use a narrow TODO/placeholder or report the gap rather than silently
creating permanent facts.

Never rewrite authored dialogue merely for code cleanup.

### Narrative file rules

Require:

- story content under `game/story/`;
- splitting by chapter and by scene only when useful;
- `script.rpy` should remain a small entry/bootstrap file;
- globally unique semantic labels;
- labels such as `prologue_start`, `ch01_apartment_door`, `ending_alone`;
- avoid labels such as `scene1`, `next`, `choice2`;
- use `call` when control should return;
- use `jump` for intentional one-way story transfer;
- explicit branch convergence;
- avoid deeply nested menus when named labels are clearer;
- do not split every few lines into separate labels;
- do not duplicate large dialogue blocks just for small state differences.

### Character rules

Shared character declarations belong in:

```text
game/definitions/characters.rpy
```

Use stable short identifiers such as:

```renpy
define mc = Character("Alex")
define lin = Character("Lin")
```

Do not redefine the same shared character in chapter files.

Do not build unnecessary Character wrappers.

### Image/asset rules

Require Codex to check the filesystem before referencing any asset filename.

Never invent/guess an asset filename.

Recommended semantic image naming:

```renpy
image bg apartment_night = "images/backgrounds/apartment_night.webp"
image lin neutral = "images/characters/lin/lin_neutral.webp"
image lin worried = "images/characters/lin/lin_worried.webp"
image cg ch01_door_open = "images/cg/ch01_door_open.webp"
```

Use lowercase snake_case filesystem names.

Keep original art/audio safe; do not destructively overwrite source assets without explicit user
instruction.

Do not silently treat placeholders as final content.

Track licensing/provenance of third-party assets before release.

### Audio rules

Preferred folders:

```text
game/audio/bgm/
game/audio/sfx/
game/audio/voice/
```

Central audio identifiers may live in:

```text
game/definitions/audio.rpy
```

but do not centralize every one-off audio file unnecessarily.

Do not add custom audio channels without a concrete need.

### Game-state rules

Use Ren'Py semantics correctly.

Saved playthrough state uses `default`.

Example:

```renpy
default trusted_lin = False
default courage = 0
default current_route = None
```

Do not initialize mutable saved state using plain init-time Python assignment.

Use `define` for constants/configuration.

Use `persistent` only for intentionally cross-save data such as:

- ending unlocks;
- gallery unlocks;
- achievements/meta progression.

Do NOT put ordinary route/chapter/current-game state into `persistent`.

Global playthrough state belongs in:

```text
game/state/variables.rpy
```

Reusable state helpers belong in:

```text
game/state/helpers.rpy
```

Prefer readable named variables over opaque numeric flags or one giant global dictionary.

### Python rules

Ren'Py script is the default.

Python is justified for:

- reusable calculations;
- deterministic helper functions;
- small data models when actually needed;
- utilities;
- integrations Ren'Py script cannot express cleanly.

Avoid Python for:

- normal dialogue sequencing;
- simple choices;
- scene changes;
- standard screen actions;
- reimplementing save/load;
- manually simulating label flow.

Do not introduce a service/repository/domain layer by default.

### UI rules

Preserve stock Ren'Py UI until customization is actually requested.

Custom project UI should live under:

```text
game/ui/
```

Prefer Ren'Py screen actions such as `Jump`, `Call`, `Show`, `Hide`, `SetVariable`, `Return` when they
clearly express the behavior.

Do not put major story logic inside screen declarations.

UI presentation is not authoritative story state.

Preserve keyboard/controller accessibility when customizing mouse-oriented UI.

Use stable element IDs when automated tests need them.

### Save compatibility

Treat save compatibility as a product concern once public builds exist.

Use `default` for newly added saved variables.

Avoid casually renaming/removing important labels after public builds.

If a future change intentionally breaks compatibility, it must be documented.

During the earliest prototype, compatibility may remain relaxed, but this must be explicit rather
than accidental.

### Focused-change discipline

Future Codex work must:

- think before coding;
- inspect existing files first;
- make focused changes only;
- avoid unrelated refactors;
- avoid speculative features;
- avoid broad renames during unrelated tasks;
- avoid rewriting generated Ren'Py files just for style;
- avoid adding abstractions without real value;
- avoid cleanup of authored prose unless explicitly requested.

### Generated/temporary files

Do not commit:

- `*.rpyc`;
- `game/cache/`;
- `game/saves/`;
- build/distribution output;
- local SDK paths;
- temporary runtime output;
- secrets/signing credentials.

Never hand-edit `.rpyc`.

### Git/external actions

`main` is the stable integration line.

Normal implementation should use focused branches.

A chapter or coherent feature milestone can use one branch; do not create one branch per tiny scene.

Do not force-push or rewrite published history.

Do not merge PRs without explicit user authorization.

Do not publish releases or upload to Steam/itch.io/stores without explicit user authorization.

Do not change remote repository settings/secrets/branch protection without explicit user
authorization.

### Validation

Meaningful `.rpy` changes must run Ren'Py lint when environment support exists.

Player-visible changes should also receive runtime validation where possible.

Use Ren'Py automated testcases for durable flows such as:

- start flow;
- important route choices;
- branch convergence;
- ending unlock logic;
- important custom screens;
- regression-prone transitions.

Lint is not a substitute for visual/runtime testing.

Never claim lint/test/runtime validation that was not actually run.

### Definition of done

Include a concise definition of done requiring the relevant subset of:

1. requested behavior/content implemented;
2. project structure respected;
3. no unrelated refactor;
4. referenced assets verified or explicitly placeholders;
5. correct state semantics;
6. lint passed where possible;
7. relevant automated tests passed;
8. relevant runtime path checked;
9. durable docs updated only when truth changed;
10. completion report states exactly what was/was not verified.

### Completion report

Future implementation reports should state:

- files changed;
- behavior/content changed;
- state/schema changes;
- assets/placeholders;
- lint/tests/runtime checks actually run;
- deferred work;
- save-compatibility concerns.

## ARCHITECTURE.md requirements

Explain that Ren'Py itself already owns much of the runtime architecture.

The project should NOT reproduce the Godot project's `core/runtime/presentation` layering.

Document this high-level model:

```text
Story
  ├── reads/writes playthrough state
  ├── invokes dialogue/scenes/choices/audio/transitions
  └── calls reusable helpers where needed

State
  ├── saved playthrough variables
  ├── persistent cross-save metadata
  └── small deterministic helpers

Definitions
  ├── characters
  ├── image mappings
  └── reusable audio identifiers

UI
  ├── project-specific screens
  └── project-specific styles

Ren'Py
  ├── save/load/rollback
  ├── menus/preferences/history
  ├── input/screen language
  ├── audio
  └── rendering/transitions
```

Explain ownership of:

- `script.rpy`;
- definitions;
- state;
- story;
- UI;
- assets;
- automated tests.

Explain:

- `script.rpy` should remain a small entry point, eventually something like:

```renpy
label start:
    jump prologue_start
```

- story labels must be globally unique and semantic;
- branching should remain readable;
- explicit image definitions may be used when they improve asset identity;
- `layeredimage` should not be introduced until actually needed;
- Ren'Py owns serialization mechanics;
- custom save repository/serializer should not be built;
- a Python domain layer becomes justified only if the VN later gains substantial systems such as
  investigation graphs, calendar simulation, complex inventory, procedural encounters, combat, or
  large relationship simulation.

Include architecture smells such as:

- giant `script.rpy`;
- character definitions scattered across chapters;
- large general-purpose Python systems inside story labels;
- screens mutating unrelated story state;
- opaque flag systems;
- Python wrappers around standard Ren'Py statements;
- custom save/load duplication;
- guessed asset paths;
- duplicated dialogue branches;
- AI inventing canon due to missing Story Bible facts.

## DEVELOPMENT.md requirements

Keep the workflow disciplined but lightweight.

Borrow the useful ideas of:

- stable main;
- focused branches;
- explicit validation;
- truthful completion reports;
- no automatic merge/release permission.

Do NOT adopt heavyweight enterprise-style phase/audit ceremony for every scene.

Recommended branch examples:

```text
feature/prologue-vertical-slice
feature/ch01-apartment
feature/custom-choice-ui
feature/gallery
fix/save-regression
fix/missing-sprite
chore/renpy-upgrade
```

Recommended lifecycle:

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

Recommended commit style examples:

```text
feat: add prologue door choice
feat: add Lin character sprite states
test: cover prologue branch convergence
fix: initialize trust state for old saves
docs: update chapter 1 canon
```

Document when to update each durable document.

Document engine upgrades as dedicated tasks rather than incidental SDK changes.

Document that local runnable output is not automatically a public release.

## STORY_BIBLE.md requirements

Create a useful template, not real story content.

Include:

- project title;
- genre;
- primary language;
- target rating/content level;
- expected playtime;
- narrative structure;
- one-sentence premise;
- player fantasy/intended experience;
- core themes;
- tone;
- what the story should not become;
- world/time period/location/world rules;
- starting player knowledge;
- hidden facts;
- timeline table;
- protagonist template;
- reusable important-character template;
- location template;
- route model;
- route-variable table;
- ending template;
- chapter outline template;
- choice-design rules;
- continuity rules;
- visual direction;
- audio direction;
- content boundaries;
- open canon questions;
- retcon/canon-change log.

Use `TBD` rather than inventing story facts.

Make it explicit that unresolved canon is not permission for Codex to silently invent canon.

## ROADMAP.md requirements

Create this initial roadmap:

### M0 — Repository and Ren'Py Foundation

Status should reflect actual progress after this task.

Goals:

- clean Ren'Py project;
- documents/tooling;
- project launches;
- lint works;
- initial smoke-test foundation;
- stable baseline.

### M1 — Playable Vertical Slice

Target roughly 5–15 minutes.

Must eventually prove:

- main menu -> Start -> story;
- background;
- character sprite/expression;
- dialogue/narration;
- BGM/SFX;
- meaningful player choice;
- state affected by choice;
- branch/convergence or small ending;
- save/load/rollback;
- automated story-flow test;
- runtime validation.

### M2 — Visual/UI Baseline

After vertical slice:

- typography;
- dialogue/name box;
- choice UI;
- quick menu decision;
- main-menu direction;
- history/save/load/preferences styling;
- accessibility;
- reference resolution/layout rules.

### M3 — Production Content Pipeline

- sprite naming/variants;
- background/CG conventions;
- audio conventions;
- asset provenance;
- chapter-production rhythm;
- Story Bible readiness.

### M4 — Chapter Production

Leave scope intentionally open until real story scope exists.

### M5 — Public Demo Release Gate

Eventually include:

- release checklist;
- save compatibility decision;
- clean Windows build;
- core-flow validation;
- placeholder cleanup;
- third-party asset provenance;
- versioning/known issues.

Do not invent dozens of speculative phases.

## STATUS.md requirements

This must describe ACTUAL state after your work.

Include:

- project name if identifiable from existing Ren'Py configuration, otherwise placeholder;
- engine 8.5.3;
- primary platform Windows;
- current milestone;
- current playable state;
- implemented foundation;
- not-yet-implemented items;
- risks/unknowns;
- next action;
- validation table.

Do not mark a check as passed unless you actually ran it.

## DECISIONS.md requirements

Create a durable decision log with a reusable decision template.

Record these initial accepted decisions:

1. Keep Ren'Py architecture lightweight.
2. Pin initial engine to Ren'Py 8.5.3.
3. Keep `main` stable; normal work uses focused branches.
4. `docs/STORY_BIBLE.md` is canonical story authority.

Do not use this file as a task journal.

## README.md requirements

Keep README concise and practical.

Include:

- project identity;
- engine version;
- Windows as initial development target;
- repository layout;
- local SDK configuration;
- commands for run/lint/test;
- links to project documents;
- first-milestone/vertical-slice strategy.

Do not claim a feature or validation result that is not true.

## .editorconfig

Use UTF-8, LF, final newline.

For `.rpy`:

- spaces;
- 4-space indentation.

For Markdown, allow intentional trailing whitespace if useful.

For PowerShell:

- spaces;
- 4-space indentation.

## .gitignore

Ignore at minimum:

```text
*.rpyc
game/cache/
game/saves/
build/
dist/
__pycache__/
*.py[cod]
.vscode/
.idea/
.DS_Store
Thumbs.db
desktop.ini
.env
.env.*
```

Also exclude common signing/credential artifacts.

Be careful not to ignore real authored runtime assets.

## Windows tool scripts

Create:

```text
tools/run.ps1
tools/lint.ps1
tools/test.ps1
```

They must NOT hardcode a machine-specific SDK path.

Use:

```powershell
$env:RENPY_SDK
```

as the SDK-root configuration.

Expected SDK location example for documentation only:

```powershell
$env:RENPY_SDK = "C:\Tools\renpy-8.5.3-sdk"
```

Resolve repository/project root relative to the script location.

For a Windows Ren'Py SDK, prefer the SDK's bundled Python executable when present, for example under:

```text
lib\py3-windows-x86_64\python.exe
```

and invoke:

```text
renpy.py <project> run
renpy.py <project> lint
renpy.py <project> test
```

The lint script should use strict automation-friendly options where supported, including an error
exit code.

However, do not blindly assume a CLI flag exists: inspect the installed SDK/help first if the SDK is
available. Make the scripts match the actual supported CLI.

The scripts should fail with a clear message if `RENPY_SDK`, Python, or `renpy.py` cannot be found.

Do not commit absolute local paths.

## Initial game-directory preparation

After inspecting the existing project, establish only the useful minimum structure.

At minimum, prepare the project for future files such as:

```text
game/definitions/
game/state/
game/story/
game/ui/
game/tests/
```

Do not add fake characters, fake story chapters, or fake production assets.

Do not rewrite `screens.rpy`, `gui.rpy`, or `options.rpy` just to move code around.

Do not replace the default `script.rpy` with invented story content.

If a tiny neutral bootstrap comment or structure change is useful, keep it minimal.

## Git discipline during this task

First inspect whether the repository already has Git initialized.

If Git is not initialized, initialize it only if normal write permissions allow it.

If there are existing user changes, preserve them.

Do not commit automatically unless the user explicitly asked for a commit in the current task.

Do not create a remote, push, PR, or merge.

## Validation

After creating the foundation:

1. Inspect the resulting repository tree.
2. Check for obvious Markdown/path inconsistencies.
3. If `RENPY_SDK` is configured and the SDK is accessible:
   - inspect the CLI/help as needed;
   - run lint;
   - run any safe initial test command if tests exist;
   - launch only if a non-interactive/safe runtime check is appropriate.
4. If the SDK is unavailable, do NOT pretend validation passed.
5. Inspect `git diff` / `git status`.

Do not manufacture a smoke test that changes the player's initial default experience unless it is
clearly isolated as a testcase.

## Final response

When finished, report:

- files created;
- existing files modified;
- directories created;
- whether Git was initialized;
- lint/test/runtime checks actually performed and results;
- anything blocked by missing `RENPY_SDK`;
- any assumptions;
- next recommended step: M1 playable vertical slice.

Do not begin M1 in this task.
