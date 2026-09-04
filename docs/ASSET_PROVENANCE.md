# Asset Provenance

This register covers M1 visual-production assets. It does not imply that prototype art is cleared or approved for public release.

## M1 production policy

- Every runtime image listed below is a fictional, AI-generated dramatized reconstruction created for this repository with Codex's built-in OpenAI image-generation tool.
- The generator identified the output as `gpt-image`; an exact public model identifier was not exposed by the tool.
- Usage basis: newly generated for this project under the user's OpenAI account and applicable service terms. No stock, archival, press, police, crime-scene, or third-party crime imagery is included. Public-release rights and credits still require a dedicated release review.
- All runtime images are 1920×1080 WebP files. They are approved for the M1 prototype, not accepted as final production art.
- Player-facing reconstruction art uses the label `AI-GENERATED DRAMATIZED RECONSTRUCTION`.
- The user-supplied sanitation-worker photograph was used only as a non-shipping reference for broad analog-documentary qualities: 35mm grain, slight softness, muted color, ambient light, and unpolished framing. Its person, location, signage, clothing, equipment, geography, and composition were not copied. The reference is not stored under `game/` and is not redistributed by this repository.

## Shared prompt standard

All generations used this shared direction, with scene-specific details added per row: fictional late-1990s Toronto; archival documentary reconstruction photographed on consumer 35mm color film; organic grain, slight softness, muted restrained color, natural ambient light, ordinary unpolished framing, period-correct materials, sober observational tone; landscape 16:9 with a calm lower area for dialogue UI; no glossy cinema lighting, glamour, sensational crime imagery, gore, blood, logos, readable text, or watermark.

Character generations referenced the approved internal identity sheets where the character appeared. Evidence generations referenced the approved story-object image so color, construction, wear, and shape would remain continuous.

## Runtime asset register

| Runtime path | Category / scene-specific prompt | Source type | Fictional person depicted | Status |
| --- | --- | --- | --- | --- |
| `game/images/m1/map/case_atlas_world.webp` | World map; unfolded atlas on a dark documentary workspace with right-side case-card space | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/establishing/toronto_rain_1998.webp` | Establishing; wet mixed residential/commercial Toronto street, overcast October 1998, period vehicles | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/victim/mara_apartment_evening.webp` | Victim scene; Mara in her modest apartment, open red umbrella drying in a shallow tray | AI-generated dramatized reconstruction | Yes — Mara Ellis | M1 prototype |
| `game/images/m1/victim/red_umbrella_by_door.webp` | Object detail; open red nylon umbrella, black curved handle, bent spoke, shallow metal tray | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/victim/answering_machine.webp` | Object detail; worn beige late-1990s corded telephone/answering machine | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/victim/film_envelope.webp` | Object detail; worn yellow processing envelope, film canister, negative strip | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/victim/refrigerator_note.webp` | Object detail; blank note pinned to an old refrigerator by a souvenir magnet | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/victim/caleb_first_visit.webp` | Victim scene; Mara at a chained apartment door and Caleb making an ordinary maintenance visit | AI-generated dramatized reconstruction | Yes — Mara Ellis and Caleb Ross | M1 prototype |
| `game/images/m1/incident/apartment_hallway_1956.webp` | Incident setting; plain dim apartment corridor at 7:56 p.m., failed light fixture | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/incident/peephole_caleb.webp` | Incident threshold; restrained peephole view of Caleb with work sheet and screwdriver | AI-generated dramatized reconstruction | Yes — Caleb Ross | M1 prototype |
| `game/images/m1/discovery/service_lane_morning.webp` | Discovery establishing; wet Toronto service lane, collection truck, worker, standalone dumpster | AI-generated dramatized reconstruction | Yes — unnamed fictional sanitation worker | M1 prototype |
| `game/images/m1/discovery/worker_opens_dumpster.webp` | Discovery action; same worker safely raises a coherent dumpster lid; interior obscured | AI-generated dramatized reconstruction | Yes — unnamed fictional sanitation worker | M1 prototype |
| `game/images/m1/discovery/worker_reaction.webp` | Discovery reaction; same worker steps back from the now-closed dumpster | AI-generated dramatized reconstruction | Yes — unnamed fictional sanitation worker | M1 prototype |
| `game/images/m1/investigation/evidence_workspace.webp` | Investigation setting; sober desk with folders, recorder, photographs, papers, and lamp | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/investigation/maintenance_storage.webp` | Resolution setting; ordinary basement maintenance room with shelves, tools, bulbs, and cleaning supplies | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/evidence/red_umbrella_evidence.webp` | Evidence photograph; matching umbrella and tray on a neutral examination table | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/evidence/answering_machine_tape.webp` | Evidence photograph; matching telephone/answering machine with cassette removed | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/evidence/film_envelope_evidence.webp` | Evidence photograph; matching envelope, canister, and negative strip with blank card/ruler | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/evidence/witness_statement.webp` | Evidence photograph; fictional statement packet with deliberately illegible pseudo-text, folder, cassette, and pen | AI-generated dramatized reconstruction | No | M1 prototype |
| `game/images/m1/memorial/mara_lake_snapshot.webp` | Memorial; candid ordinary-life snapshot of Mara alive beside an Ontario lake | AI-generated dramatized reconstruction | Yes — Mara Ellis | M1 prototype |

## Internal identity references

These files support character continuity and are not runtime images:

| Path | Purpose | Source type | Status |
| --- | --- | --- | --- |
| `reference/visual/m1/mara_identity_reference.png` | Canonical M1 face, hair, body, and everyday clothing reference for Mara | AI-generated fictional identity sheet | Internal prototype reference |
| `reference/visual/m1/caleb_identity_reference.png` | Canonical M1 face, hair, body, glasses, and workwear reference for Caleb | AI-generated fictional identity sheet | Internal prototype reference |
| `reference/visual/m1/rachel_identity_reference.png` | Canonical family resemblance and distinct facial structure reference for Rachel | AI-generated fictional identity sheet | Internal prototype reference |

## Rejected generations

Two first attempts were rejected and never copied into runtime assets: the first apartment scene showed the umbrella closed, and the first service-lane image contained an incoherent attached container. Corrected generations replaced both. Raw tool outputs remain outside the repository in the local Codex generation cache.
