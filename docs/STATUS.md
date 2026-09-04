# Project Status

## Snapshot

| Field | Actual state |
| --- | --- |
| Project name | MyVisualNovel (working repository identity; final product title remains TBD) |
| Supported engine | Ren'Py 8.5.3 |
| Primary platform | Windows |
| Current branch | `feature/m1-vertical-slice` |
| Current milestone | M1 — Playable Vertical Slice |
| Playable content | One implemented fictional composite prototype case: `The Red Umbrella` |

## Implemented foundation and M1 content

- M0 repository policy, documentation, structure, Git ignore rules, and Windows SDK scripts
- Small `script.rpy` entry that opens the anthology world map
- Ren'Py-native temporary world-map presentation with one active Toronto node and reusable case-card capacity
- Explicit fictional-composite and content notices
- Mara Ellis victim-perspective sequence with umbrella, answering machine, film, and household-note interactions
- Restrained incident-threshold and sanitation-worker discovery sequences without graphic imagery
- Distinct documentary investigation perspective
- Reusable evidence viewer separating known fact, inference, and unconfirmed interpretation
- Lightweight investigation timeline
- Guided contradiction interaction with non-punitive retry
- Reinterpretation of earlier lived details, delayed resolution, conviction, person-centered memorial, and return to map
- Save-state-only case completion indication
- Product canon, editorial boundaries, research policy, and media provenance rules

## M1 state

Five Boolean variables use Ren'Py `default`: four victim-scene attention flags and one playthrough completion flag. No `persistent` state, custom serializer, inventory, backend, or case database exists.

## Assets and presentation

- No third-party, authentic crime, archival, or AI-generated media was added.
- M1 visuals are plain Ren'Py `Solid` displayables and text panels labeled as reconstruction/development placeholders.
- No production audio exists; no nonexistent audio files are referenced.
- Stock `screens.rpy`, `gui.rpy`, `options.rpy`, GUI assets, font, save/load, rollback, preferences, history, and accessibility behavior remain intact.

## Not yet implemented

- Verified Ren'Py automated testcase; syntax support cannot be confirmed without the SDK
- Final world-map or reconstruction artwork
- Production music, ambience, SFX, or voice
- Real-case research, source records, archival material, or licensing review
- Multiple cases, content database, advanced map, inventory, or forensic simulation
- Final title, primary language/localization strategy, rating, and release policy
- M2 visual/UI baseline or any release work

## Risks and unknowns

- `RENPY_SDK` is not configured in the current environment, so fresh Ren'Py lint, automated tests, and runtime/manual route checks are blocked.
- Screen-language and script structure receive static review only until engine lint/runtime are available.
- The prototype narrative is fictional, but its location is real; every player-facing entry and closing must keep the fictional-composite notice visible.
- M1 prototype text is currently English while the stock generated UI is Simplified Chinese; primary product language remains unresolved canon.

## Next action

Configure the Ren'Py 8.5.3 SDK, run lint, add or validate one critical-flow testcase using confirmed 8.5.3 syntax, and manually play the complete route. Review M1 before any commit or integration. Do not begin M2 until M1 validation and user review are complete.

## Validation

| Check | Result | Evidence / limitation |
| --- | --- | --- |
| Branch started from clean `main` | Passed | Created `feature/m1-vertical-slice` before edits |
| Required files and focused architecture | Passed | Final tree and diff inspected; stock UI/options remain untouched |
| Generated artifact ignore rules | Passed | Compiled scripts, cache, saves, and runtime log remain ignored |
| Static labels/state/assets review | Passed | 14 unique labels, 22 resolved jumps, 4 resolved screen calls; no persistent, URL, or external asset references |
| Ren'Py lint | Blocked | `RENPY_SDK` is not set |
| Ren'Py automated test | Blocked | SDK/testcase syntax unavailable; no unverified testcase added |
| Runtime/manual route | Blocked | `RENPY_SDK` is not set |
