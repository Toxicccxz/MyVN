# Architecture

## Principle

Ren'Py already owns most runtime architecture. This project does not reproduce Godot-style `core/runtime/presentation/application` layering and does not add service, repository, controller, or domain layers without a demonstrated feature need.

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

## Ownership

- `game/script.rpy` is a small bootstrap and entry point. Once real content exists it should normally resemble:

  ```renpy
  label start:
      jump prologue_start
  ```

- `game/definitions/` owns shared characters, explicit image mappings, and reusable audio identifiers.
- `game/state/` owns `default` playthrough variables, deliberately persistent cross-save metadata, and small deterministic helpers.
- `game/story/` owns narrative flow, dialogue, choices, scenes, transitions, and ordinary audio playback.
- `game/ui/` owns project-specific screens and styles. Stock `screens.rpy` and `gui.rpy` remain in place until a real customization requires change.
- `game/images/`, `game/audio/`, and `game/fonts/` own runtime assets, organized semantically as the asset set grows.
- `game/tests/` owns isolated Ren'Py automated testcases for durable player flows and regression-prone behavior.

The anthology shell is implemented with ordinary Ren'Py screens under `game/ui/`: the world-map screen selects a case and returns a semantic result to story flow; the evidence viewer and timeline present investigation information without owning story outcomes. Case narrative remains in `game/story/`, and completion remains ordinary `default` playthrough state. Adding a future case should extend the shell without introducing a map engine, backend, or content database unless scale later proves one necessary.

Story labels are globally unique and semantic. Branches should make divergence and convergence easy to read. Use `call` for returning subflows and `jump` for intentional one-way transfer.

Explicit image definitions are useful when they strengthen semantic asset identity. Do not add `layeredimage` until the actual sprite workflow needs it, and never guess asset paths.

## State and serialization

Ren'Py owns serialization, save/load, rollback, preferences, and related compatibility mechanics. Saved playthrough variables use `default`; cross-save `persistent` state is reserved for intentional meta progression. Do not build a custom save repository, serializer, or wrapper around standard Ren'Py statements.

A Python domain layer becomes reasonable only if the VN develops substantial systems—such as investigation graphs, calendar simulation, complex inventory, procedural encounters, combat, or a large relationship simulation—that Ren'Py script and small helpers cannot express cleanly.

## Architecture smells

- A giant `script.rpy`
- Character definitions scattered across chapters
- Large general-purpose Python systems inside story labels
- Screens mutating unrelated story state
- Opaque flags or a single giant state dictionary
- Python wrappers around standard Ren'Py statements
- Custom save/load duplication
- Guessed asset paths
- Duplicated dialogue branches for minor state differences
- AI inventing canon because the Story Bible is unresolved
