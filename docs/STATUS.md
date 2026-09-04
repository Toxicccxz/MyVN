# Project Status

## Snapshot

| Field | Actual state |
| --- | --- |
| Project name | MyVisualNovel (from `config.name`) |
| Supported engine | Ren'Py 8.5.3 |
| Primary platform | Windows |
| Current milestone | M0 — Repository and Ren'Py Foundation |
| Playable state | Stock generated Ren'Py sample only; no authored story content |

## Implemented foundation

- Stock generated `script.rpy`, `screens.rpy`, `gui.rpy`, `options.rpy`, GUI assets, font, and template experience preserved
- Repository initialized locally on `main` with generated/runtime artifacts ignored
- Codex project policy and durable project documents established
- Lightweight `definitions`, `state`, `story`, `ui`, and `tests` directories prepared
- Windows run/lint/test scripts driven by `RENPY_SDK`
- Ren'Py 8.5.3 confirmed in the existing local runtime log

## Not yet implemented

- Real premise, canon, characters, routes, or authored dialogue
- M1 playable vertical slice
- Production art, music, SFX, voice, or asset provenance records
- Custom project UI or styles
- Automated Ren'Py testcases
- Public-build and save-compatibility policy

## Risks and unknowns

- Story scope, language, tone, content boundaries, and all permanent canon remain TBD.
- `RENPY_SDK` is not configured in the current environment, so the new scripts and current source have not yet received fresh engine-backed lint/test/runtime validation.
- The stock sample uses Ren'Py-generated placeholder character/background images, not production assets.
- The repository has no initial commit or remote; external repository workflow is not yet established.

## Next action

Configure a local Ren'Py 8.5.3 SDK, run M0 lint/test/runtime validation, then begin M1 as a 5–15 minute playable vertical slice after the necessary Story Bible canon is authored.

## Validation

| Check | Result | Evidence / limitation |
| --- | --- | --- |
| Foundation tree inspection | Passed | Required root/docs/tools files and prepared game directories exist |
| Markdown/path consistency | Passed | Required headings, documented relative links, and repository paths checked locally |
| PowerShell syntax | Passed | All three scripts parsed without errors |
| Missing-SDK failure behavior | Passed | Scripts stop with a clear `RENPY_SDK is not set` error |
| Git ignore rules | Passed | Compiled scripts, cache, saves, and runtime log verified ignored |
| Ren'Py lint | Blocked | `RENPY_SDK` not set in current environment |
| Ren'Py automated tests | Blocked | `RENPY_SDK` not set; no testcases exist yet |
| Fresh runtime check | Blocked | `RENPY_SDK` not set; existing `log.txt` records a prior Ren'Py 8.5.3 startup only |
