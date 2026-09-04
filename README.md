# MyVisualNovel

`MyVisualNovel` is a Ren'Py visual novel project. The supported engine is **Ren'Py 8.5.3**, and Windows is the initial development and release target. The repository currently preserves the stock generated project as its baseline; real story production begins with the M1 vertical slice.

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

## First production milestone

M1 is a focused 5–15 minute playable vertical slice proving the complete player path and production workflow: start flow, visuals, audio, dialogue, a meaningful stateful choice, convergence or a small ending, stock save/load/rollback, an automated flow test, lint, and runtime validation. It should validate the VN pipeline without becoming a general-purpose framework.

