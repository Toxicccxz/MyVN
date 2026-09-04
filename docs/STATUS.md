# Project Status

## Snapshot

| Field | Actual state |
| --- | --- |
| Project name | MyVisualNovel (working repository identity; final product title remains TBD) |
| Supported engine | Ren'Py 8.5.3 |
| Primary platform | Windows |
| Current branch | `feature/m1-vertical-slice` |
| Current milestone | M1 — Playable Vertical Slice, visual production pass integrated |
| Playable content | One implemented fictional composite prototype case: `The Red Umbrella` |

## Implemented foundation and M1 content

- M0 repository policy, documentation, structure, Git ignore rules, and Windows SDK scripts
- Small `script.rpy` entry that opens the anthology world map
- Generated atlas presentation with one programmatic active Toronto node and reusable case-card capacity
- Explicit fictional-composite and content notices
- Mara Ellis victim-perspective sequence with umbrella, answering machine, film, and household-note interactions
- Restrained incident-threshold and sanitation-worker discovery sequences without graphic imagery
- Distinct documentary investigation perspective
- Reusable illustrated evidence viewer separating known fact, inference, and unconfirmed interpretation
- Lightweight investigation timeline
- Guided contradiction interaction with non-punitive retry
- Reinterpretation of earlier lived details, delayed resolution, conviction, person-centered memorial, and return to map
- Save-state-only case completion indication
- Product canon, editorial boundaries, research policy, and media provenance rules
- Twenty integrated 1920×1080 WebP runtime images plus three non-runtime character identity references
- Consistent player-facing `AI-GENERATED DRAMATIZED RECONSTRUCTION` labeling

## M1 state

Five Boolean variables use Ren'Py `default`: four victim-scene attention flags and one playthrough completion flag. No `persistent` state, custom serializer, inventory, backend, or case database exists.

## Assets and presentation

- M1 includes 20 fictional AI-generated dramatized reconstruction images under `game/images/m1/`, each verified as 1920×1080 WebP.
- Mara, Caleb, and Rachel have approved internal identity references under `reference/visual/m1/`; Rachel's sheet is a continuity reference and is not loaded at runtime.
- The world map, establishing shot, victim apartment and objects, maintenance visits, restrained discovery actions, investigation spaces, evidence items, and memorial all use the generated pass.
- Every asset's source type, usage basis, fictional-person status, prompt summary, and prototype approval stage is recorded in `docs/ASSET_PROVENANCE.md`.
- No third-party, authentic crime, archival, press, police, or stock media was added. The user's style reference is not stored under `game/` or redistributed in the repository.
- No production audio exists; no nonexistent audio files are referenced.
- Stock `screens.rpy`, `gui.rpy`, `options.rpy`, GUI assets, font, save/load, rollback, preferences, history, and accessibility behavior remain intact.

## Not yet implemented

- Final public-release artwork and release-rights review; the integrated visual pass remains M1 prototype art
- Production music, ambience, SFX, or voice
- Real-case research, source records, archival material, or licensing review
- Multiple cases, content database, advanced map, inventory, or forensic simulation
- Final title, primary language/localization strategy, rating, and release policy
- M2 visual/UI baseline or any release work

## Risks and unknowns

- A temporary official Ren'Py 8.5.3 SDK was used successfully for this pass, but `RENPY_SDK` is still not persistently configured for future sessions.
- The automated route test bypasses the title-card and investigation call-screen buttons after asserting the screens appeared because the test runner could not reliably activate those modal buttons. Their screen definitions lint, and the evidence viewer has a separate engine render test; a human should still verify button focus and final text fit.
- The prototype narrative is fictional, but its location is real; every player-facing entry and closing must keep the fictional-composite notice visible.
- M1 prototype text is currently English while the stock generated UI is Simplified Chinese; primary product language remains unresolved canon.

## Next action

Persistently configure the Ren'Py 8.5.3 SDK and manually review the complete route with special attention to evidence-viewer text fit, modal-button focus, world-map marker placement, and dialogue readability. Do not begin M2 until user review is complete.

## Validation

| Check | Result | Evidence / limitation |
| --- | --- | --- |
| Branch started from clean `main` | Passed | Created `feature/m1-vertical-slice` before edits |
| Required files and focused architecture | Passed | Final tree and diff inspected; stock UI/options remain untouched |
| Generated artifact ignore rules | Passed | Compiled scripts, cache, saves, and runtime log remain ignored |
| Runtime asset format audit | Passed | 20 runtime files; all decode as WebP at exactly 1920×1080 |
| Asset mapping audit | Passed | 20 unique semantic mappings; every referenced `images/m1` file exists |
| Visual QA | Passed | All selected generations and representative final WebP crops inspected; two defective first generations were rejected and replaced |
| Static labels/state/assets review | Passed | Unique labels and resolved jumps rechecked; five existing `default` variables unchanged; no persistent state or external runtime asset references |
| Git diff hygiene | Passed | `git diff --check` passed; no generated Ren'Py cache/save/build output present |
| Ren'Py lint | Passed | Official Ren'Py 8.5.3.26051504, zero lint findings |
| Ren'Py automated route | Passed with documented harness bypass | `m1_complete_visual_route`: map, all four apartment inspections, incident option, discovery, contradiction, resolution, memorial, completion state, and return to map; modal call-screen buttons are bypassed after presence assertions |
| Evidence viewer render | Passed | `m1_evidence_viewer_renders` displayed the image-enabled screen in Ren'Py 8.5.3 |
| Runtime launch | Passed | Game initialized the GL2 renderer without traceback at virtual/physical/drawable 1920×1080 |
| Human full-route visual review | Not run | Generated assets and representative final crops were inspected, but the complete route was not manually played through in the visible game window |
