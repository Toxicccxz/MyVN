# Codex Project Policy

## Mission

This repository is a Ren'Py visual novel targeting Ren'Py 8.5.3, with Windows as the initial development platform. Keep it easy to understand, review, and maintain through AI-assisted development. It is a visual novel first: use Ren'Py's existing features and avoid building a general-purpose game framework.

## Sources of truth

- `docs/STORY_BIBLE.md` owns canonical story, world, character, tone, and continuity facts.
- `docs/ARCHITECTURE.md` owns stable technical structure and boundaries.
- `docs/DEVELOPMENT.md` owns development, Git, and validation workflow.
- `docs/ROADMAP.md` owns planned milestones.
- `docs/STATUS.md` owns the actual current project state.
- `docs/DECISIONS.md` records durable decisions future work should not repeatedly reopen.
- The actual `.rpy` implementation owns actual implemented runtime behavior.

If documentation and implementation conflict, inspect the surrounding context and report or resolve the discrepancy deliberately. Never silently choose one source.

## Story authority

Before adding important story facts, inspect the Story Bible and relevant chapter files. Canon includes character identity, age, history, relationships, motivation, personality, knowledge, chronology, world rules, locations, route requirements, ending conditions, established visual traits, and tone/content boundaries.

Do not invent permanent canon when a task does not provide it. If missing canon is necessary, use a narrow `TODO`/placeholder or report the gap. Unresolved canon is not permission to improvise permanent facts. Never rewrite authored dialogue merely for code cleanup.

## Narrative files and flow

- Put story content under `game/story/`; split by chapter and then scene only when that improves navigation.
- Keep `game/script.rpy` a small entry/bootstrap file.
- Use globally unique semantic labels such as `prologue_start`, `ch01_apartment_door`, and `ending_alone`; avoid `scene1`, `next`, or `choice2`.
- Use `call` when control should return and `jump` for intentional one-way transfer.
- Make branch convergence explicit. Prefer named labels to deeply nested menus.
- Do not split every few lines into labels or duplicate large dialogue blocks for small state differences.

## Characters

Shared character declarations belong in `game/definitions/characters.rpy`. Use stable short identifiers, for example:

```renpy
define mc = Character("Alex")
define lin = Character("Lin")
```

Do not redefine a shared character in chapter files or build unnecessary `Character` wrappers.

## Images and assets

Check the filesystem before referencing an asset. Never invent or guess filenames. Use lowercase snake_case filesystem names and semantic mappings when helpful:

```renpy
image bg apartment_night = "images/backgrounds/apartment_night.webp"
image lin neutral = "images/characters/lin/lin_neutral.webp"
image lin worried = "images/characters/lin/lin_worried.webp"
image cg ch01_door_open = "images/cg/ch01_door_open.webp"
```

Keep original art and audio safe; do not destructively overwrite source assets without explicit user instruction. Do not silently treat placeholders as final. Track third-party licensing and provenance before release.

## Audio

Prefer `game/audio/bgm/`, `game/audio/sfx/`, and `game/audio/voice/`. Reusable identifiers may live in `game/definitions/audio.rpy`, but do not centralize every one-off file. Do not add custom audio channels without a concrete need.

## Game state

Use `default` for saved playthrough state:

```renpy
default trusted_lin = False
default courage = 0
default current_route = None
```

Do not initialize mutable saved state with plain init-time Python assignment. Use `define` for constants and configuration. Use `persistent` only for intentional cross-save data such as ending/gallery unlocks, achievements, or meta progression—never for current route, chapter, or ordinary playthrough state.

Global playthrough state belongs in `game/state/variables.rpy`; reusable state helpers belong in `game/state/helpers.rpy`. Prefer readable named variables over opaque numeric flags or one giant dictionary.

## Python

Ren'Py script is the default. Python is appropriate for reusable calculations, deterministic helpers, small data models that are actually needed, utilities, and integrations Ren'Py cannot express cleanly. Do not use it for ordinary dialogue, simple choices, scene changes, normal screen actions, label-flow simulation, or replacements for save/load. Do not introduce service, repository, controller, or domain layers by default.

## UI

Preserve stock Ren'Py UI until customization is requested. Put project-specific screens and styles under `game/ui/`. Prefer standard actions such as `Jump`, `Call`, `Show`, `Hide`, `SetVariable`, and `Return` when they express behavior clearly. Keep major story logic out of screens; presentation is not authoritative story state. Preserve keyboard/controller accessibility and use stable element IDs where automated tests need them.

## Save compatibility

Treat save compatibility as a product concern once public builds exist. Use `default` for newly added saved variables and avoid casually renaming or removing important labels after release. Document intentional compatibility breaks. Compatibility may be relaxed during the earliest prototype, but only as an explicit decision.

## Focused-change discipline

Think before coding and inspect existing files first. Make focused changes; avoid unrelated refactors, speculative features, broad renames, style-only rewrites of generated files, premature abstractions, and cleanup of authored prose unless requested.

## Generated and temporary files

Do not commit `*.rpyc`, `*.rpymc`, `game/cache/`, `game/saves/`, build/distribution output, local SDK paths, temporary runtime output, secrets, or signing credentials. Never hand-edit compiled Ren'Py files.

## Git and external actions

`main` is the stable integration line. Use focused branches for normal implementation; one chapter or coherent milestone may share a branch, but do not create a branch for every tiny scene. Never force-push or rewrite published history. Do not merge PRs, publish releases, upload to stores, or change remote settings, secrets, or branch protection without explicit user authorization.

## Validation

Run Ren'Py lint for meaningful `.rpy` changes when the environment supports it. Player-visible changes also need runtime validation where possible. Add Ren'Py testcases for durable flows such as startup, important route choices, branch convergence, ending unlock logic, important custom screens, and regression-prone transitions. Lint does not replace visual/runtime testing. Never claim a check that was not run.

## Definition of done

Apply the relevant subset:

1. Requested behavior or content is implemented.
2. Project structure is respected.
3. No unrelated refactor was introduced.
4. Referenced assets were verified or are explicitly placeholders.
5. State uses correct Ren'Py semantics.
6. Lint passed where possible.
7. Relevant automated tests passed.
8. Relevant runtime paths were checked.
9. Durable docs changed only when project truth changed.
10. The completion report says exactly what was and was not verified.

## Completion reports

Report files changed, behavior/content changes, state/schema changes, assets/placeholders, lint/tests/runtime checks actually run, deferred work, and save-compatibility concerns.
