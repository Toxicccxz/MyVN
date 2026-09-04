# MyVisualNovel

`MyVisualNovel` is the working repository identity for a documentary-style interactive true-crime anthology; the final product title remains TBD. The supported engine is **Ren'Py 8.5.3**, and Windows is the initial development and release target. M1 implements one clearly fictional composite prototype case, `The Red Umbrella`, to prove the format before any researched real-case production.

## Repository layout

- `game/` — Ren'Py source, generated default UI, and runtime assets
- `game/definitions/` — shared character, image, and reusable audio definitions
- `game/state/` — saved variables and small reusable helpers
- `game/story/` — narrative flow organized by chapter/scene when useful
- `game/ui/` — project-specific screens and styles
- `game/tests/` — Ren'Py automated testcases
- `docs/` — architecture, workflow, canon template, roadmap, status, and decisions
- `tools/` — Windows run, lint, and test entry points

## Local SDK configuration

Install the Ren'Py 8.5.3 SDK and set `RENPY_SDK` to its root for the current PowerShell session. Do not store a machine-specific path in the repository.

```powershell
$env:RENPY_SDK = "C:\Tools\renpy-8.5.3-sdk"
```

The scripts prefer the SDK's bundled Windows Python and fall back to `python.exe` on `PATH` only when necessary. They fail clearly when the SDK, Python, or `renpy.py` cannot be found.

```powershell
.\tools\run.ps1
.\tools\lint.ps1
.\tools\test.ps1
```

## Project documents

- [Architecture](docs/ARCHITECTURE.md)
- [Development workflow](docs/DEVELOPMENT.md)
- [Story Bible](docs/STORY_BIBLE.md)
- [Roadmap](docs/ROADMAP.md)
- [Current status](docs/STATUS.md)
- [Decision log](docs/DECISIONS.md)

## Current vertical slice

M1 provides a focused 10–15 minute flow: world-map selection, victim-perspective ordinary life, a restrained incident threshold and discovery, evidence/timeline interpretation, resolution, memorial, and return to the map. It uses only labeled Ren'Py-native visual placeholders and no third-party crime media. Engine lint, automated-test syntax, and runtime validation remain blocked until `RENPY_SDK` is configured.
