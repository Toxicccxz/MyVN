# Story Bible

This document is the canonical authority for story, world, character, tone, and continuity. `TBD` means unresolved; it is not permission for Codex to silently invent permanent canon.

## Project identity

| Field | Canon |
| --- | --- |
| Final project title | TBD |
| Genre | Documentary-style interactive visual novel / interactive true-crime anthology |
| Primary language | TBD |
| Target rating/content level | TBD; intended for a mature audience because cases concern homicide and disturbing themes |
| Expected playtime | Anthology scope TBD; M1 prototype case targets 10–15 minutes |
| Narrative structure | World-map anthology of self-contained cases using victim-before-crime and investigation-after-crime perspectives |

## Core premise and intended experience

The player explores a world map containing homicide cases from different countries and historical periods. Selecting a location opens a self-contained case.

The intended experience is **narrative investigation + light interaction + evidence interpretation**, not a complex police simulator. The player participates in understanding the case but is not an omnipotent detective who personally performs every police action.

### Perspective A — Before the crime

The player follows the victim through ordinary routines, work, relationships, mundane choices, messages, objects, places, subtle warning signs, and details that later become evidence. This perspective builds empathy and presents the victim as a person rather than a statistic. It should not treat the victim as though they know they are in a horror story.

### Perspective B — After the crime

The viewpoint changes to a restrained third-person documentary reconstruction. The player follows discovery, investigation, conflicting testimony, evidence, errors, breakthroughs, and the eventual outcome or unresolved status. Interaction supports attention and comprehension rather than fantasy police procedure.

## Core creative principle

> The victim is a person first and a case second.

The project does not sell murder as spectacle. Its emotional force should come from knowing the victim before knowing the case, recognizing earlier objects as evidence, information asymmetry, delayed understanding, irony, missed opportunities, contradictory testimony, investigative breakthroughs, the contrast between ordinary life and later events, and the human consequences of violence.

## Canonical case structure

```text
World Map
    ↓
Case Selection
    ↓
Case Introduction / Content Notice
    ↓
Victim Perspective
    ↓
Incident Threshold
    ↓
Discovery
    ↓
Investigation
    ↓
Evidence / Timeline / Contradictions
    ↓
Truth or Current Best Reconstruction
    ↓
Judicial / Investigative Outcome
    ↓
Victim Memorial / Reflection
    ↓
Return to World Map
```

Scene count may vary by case, but completed cases need emotional closure and must return attention to the victim. A resolved case may emphasize accountability. An unresolved case may emphasize uncertainty, loss, and unanswered questions. Do not force a simplistic moral such as “good always wins.” A closing should normally express the idea: **Remember the person, not only the crime.**

## Interaction philosophy

Interaction exists to increase presence, attention, memory, narrative pacing, and investigative understanding—not merely to appear game-like.

Preferred interactions include world-map case selection, inspecting objects, opening doors or containers, checking messages or an answering machine, examining photographs, selecting evidence, reviewing a timeline, comparing testimony, identifying contradictions, and connecting earlier-life details to later evidence.

Avoid unrelated minigames and complex inventory mechanics. Historical outcomes are not game-over puzzles.

## Choice philosophy

- **Narrative attention choices:** determine what the player notices or inspects.
- **Character-expression choices:** express personality or routine without rewriting historical outcomes.
- **Investigation-order choices:** determine which evidence the player examines first.
- **Interpretation choices:** ask what appears important or contradictory; errors should guide rather than punish.
- **True branch choices:** reserved for fictional narratives or situations that genuinely diverge.

For documented cases, never imply that a player could casually prevent a real victim's death with a dialogue choice.

## Violence presentation

- Graphic gore is not the attraction or default visual language.
- Do not linger on physical killing mechanics or include unnecessary procedural detail.
- Do not recreate prolonged assault as entertainment or create a playable murder simulation.
- Victim-perspective sequences normally stop at or around the incident threshold.
- Discovery may strongly imply disturbing findings without explicit anatomy.
- Prefer sound, framing, reaction, text, omission, and aftermath to excessive visual detail.
- Graphic material requires a later explicit decision and a clear documentary/narrative purpose.
- The work may be emotionally disturbing where the subject requires it, but never gratuitous or gore tourism.

## Media authenticity and provenance

Future cases may combine licensed/publicly usable authentic archival material, game-created diagrams and documents, AI-generated documentary reconstruction, original artwork/sound, and textual reconstruction. These categories must remain distinguishable in credits and case sources:

```text
Authentic archival material
Recreated / dramatized material
AI-generated reconstruction
Original game artwork
```

AI or recreated imagery must never be presented as authentic crime-scene, police, press, or historical photography. Do not use recognizable news-brand layouts or marks to manufacture false authenticity.

M1 uses only clearly labeled fictional AI-generated dramatized reconstruction art. It includes no authentic archival media, third-party crime media, or production audio. Every M1 runtime image is registered in `docs/ASSET_PROVENANCE.md` and shown with the label `AI-GENERATED DRAMATIZED RECONSTRUCTION`.

## Documentary visual direction

- Restrained documentary tone with late-1990s archival influence where relevant
- Understated typography and subdued, low-gloss interface
- Dates and locations as strong visual anchors
- Case-file and evidence language
- Reconstruction images use a consumer-35mm documentary language: visible grain, slight softness, muted color, ambient light, and ordinary, imperfect framing
- All AI-generated M1 imagery is visibly labeled `AI-GENERATED DRAMATIZED RECONSTRUCTION`
- Minimal flashy game UI

Avoid blood-splatter menus, pervasive police-tape clichés, excessive glitch effects, exaggerated “serial killer wall” aesthetics, fake branded news channels, and sensational tabloid styling. The project should feel closer to an interactive documentary than arcade horror.

## Audio direction

Victim-perspective audio favors ordinary environment, rain, apartment ambience, distant traffic, answering-machine cues, and subtle music only when appropriate. Investigation audio favors restrained documentary scoring, room tone, tape playback, and understated evidence/UI sounds. Avoid repeated horror stingers.

M1 references no audio files because no production assets exist. Its sound moments are conveyed textually until sourced original audio is available.

## World and anthology rules

- **Geographic model:** real geographic locations presented through a world-map case shell.
- **Time periods:** may vary by case; chronology must be researched and explicit.
- **World rules:** documentary framing must distinguish fact, inference, disputed claims, and reconstruction.
- **Starting player knowledge:** only the case card, location/year, fictional/documented status, and content notice.
- **Hidden facts:** case-specific; never reveal knowledge through a character who could not possess it.
- **Full anthology scope:** TBD. No future case canon is established by M1.

## M1 prototype case — The Red Umbrella

### Status and boundaries

`The Red Umbrella` is an internal M1 case title, not the final game title. It is a **fictional composite case** created for prototype development, set in the real location Toronto, Canada, in October 1998. It is not based on one identifiable murder. No real victim, offender, or historical homicide is depicted.

### Mara Ellis

| Field | Canon |
| --- | --- |
| Name / identifier | Mara Ellis / `mara` |
| Age | 29 |
| Location / year | Toronto, Canada / 1998 |
| Occupation | Employee at a small independent photo lab |
| Living situation | Lives alone in a modest apartment |
| Personality | Observant, practical, somewhat private, dislikes confrontation |
| Interests | Enjoys photography but does not consider herself an artist |
| Habits | Keeps small receipts, notes, and undeveloped film longer than necessary |
| Relationships | Maintains close contact with her older sister Rachel; works with Samir Patel |
| Visual identity | Light olive complexion; shoulder-length naturally wavy dark-brown hair; hazel-brown eyes; softly angular face; small mole near the left eyebrow; average build |
| M1 clothing | Navy wool cardigan over a muted rust blouse with tan straight-leg trousers; denim jacket over the same muted rust blouse in the lake snapshot |
| Continuity rule | Her ordinary life is established without foreknowledge or horror-protagonist behavior |

### Supporting characters

| Character | Role and canonical purpose |
| --- | --- |
| Rachel Ellis | Mara's older sister; establishes family connection, routine, personal belongings, and person-centered remembrance |
| Samir Patel | Mara's coworker; establishes photo-lab life and lends her the red umbrella during heavy rain |
| Caleb Ross | Building superintendent; initially ordinary and helpful, later contradicted by timeline and physical evidence; ultimately arrested and convicted |
| Documentary record | Neutral post-crime investigative voice, not a superhero detective or player avatar |

Do not expand the M1 cast unless a concrete requirement cannot be met otherwise.

### M1 visual canon

- **Caleb Ross:** white Canadian man in his early forties; average build; thinning sandy-brown hair; pale gray-blue eyes; rectangular face; faint under-eye lines; clean-shaven; thin wire-rim glasses; faded gray-green work jacket over a muted brown plaid shirt. His presentation is ordinary and non-theatrical rather than visually coded as threatening.
- **Rachel Ellis:** thirty-four; light olive complexion, hazel-brown eyes, and dark-brown hair that establish family resemblance to Mara, with a distinct rounder jaw, broader nose, faint smile lines, and practical chin-length bob. Her reference clothing is an oatmeal knit sweater over a muted blue shirt.
- **Mara/Rachel resemblance:** strong enough to read as sisters, never as duplicates. Their separate facial structure, age, hairstyle, and clothing must remain visible.
- **Unnamed sanitation worker:** a wholly fictional, anonymous municipal worker. The worker's design is not based on the person in the external style-reference photograph.
- M1 reconstruction art remains restrained, non-glamorous, and free of gore. Evidence and pseudo-documents must not contain invented readable official text.

### Locations

| Location | Purpose / visual treatment |
| --- | --- |
| World map | Reusable anthology shell; generated atlas texture with one programmatically positioned active Toronto node; the node, not painted geography, is authoritative |
| Bellweather Photo Lab | Mara's workplace context; referenced rather than separately staged in M1 |
| Mara's apartment/building | Ordinary victim-perspective space; entry, answering machine, film, note, latch, corridor |
| Commercial service lane | Next-morning discovery; implied through framing and reaction without graphic imagery |
| Investigation record | Generated documentary workspace and evidence photographs, with programmatic text retaining authority over facts and interpretation |

### Narrative devices

**Red umbrella:** Samir lends it to Mara during heavy rain. The player sees it drying inside her entrance before it becomes evidence. A tenant places Mara entering the building with it; its later absence and recovery from maintenance storage contribute to exposing Caleb's contradictory account. It is one corroborating item, not a magical solution.

**Answering machine:** Rachel leaves an ordinary Sunday-dinner reminder. Caleb leaves a mundane maintenance message saying he will inspect the sticking latch before eight. The preserved timing and wording later contradict his denial of a planned visit but do not solve the case alone.

**Film envelope and refrigerator note:** These establish Mara's photography, habits, family plans, and unfinished ordinary life. The film envelope's movement later corroborates other evidence.

### M1 timeline

| Time | Event | Status |
| --- | --- | --- |
| October 1998, 6:35 p.m. | Mara leaves the photo lab with Samir's red umbrella | Known fact in reconstruction |
| 7:03 p.m. | A tenant sees Mara enter her building with the umbrella | Known fact in reconstruction |
| 7:08 p.m. | Caleb's maintenance message is recorded | Known fact |
| Before 8:00 p.m. | Caleb is expected to return to inspect the latch | Supported by recording and Mara's experience |
| 7:56 p.m. onward | Incident threshold and probable incident window | Exact physical sequence deliberately not depicted |
| Following morning | Suspicious human remains are discovered on a municipal route | Known fact; no graphic presentation |
| Following months | Statements, access records, recovered property, trace evidence, and testimony converge | Investigative reconstruction |
| Later judicial outcome | Caleb is arrested, tried, and convicted | Fictional case outcome |

### M1 route and state model

The prototype is a primarily linear case with attention choices, evidence-order choice, and a guided interpretation question. Incident outcome does not branch. Wrong interpretation returns a restrained explanation and another attempt. Completion returns to the world map.

| Variable | Type/default | Meaning |
| --- | --- | --- |
| `m1_red_umbrella_seen` | Boolean / `False` | Player inspected the umbrella in Mara's apartment |
| `m1_answering_machine_checked` | Boolean / `False` | Player heard Rachel's and Caleb's messages |
| `m1_photo_checked` | Boolean / `False` | Player inspected Mara's film envelope |
| `m1_kitchen_note_seen` | Boolean / `False` | Player read Mara's ordinary reminder note |
| `m1_case_completed` | Boolean / `False` | Current playthrough completed the case |

All are ordinary save-state variables declared with `default`; none is persistent cross-save metadata.

### M1 ending

The case establishes Caleb's contradictory accounts, corroborating evidence, arrest, and conviction without recreating crime mechanics. The final reflection returns to Mara's photographs, relationship with Rachel, small habits, and unfinished plans. It repeats the fictional-composite notice before returning to the map.

## Continuity and editorial rules

- Check character knowledge, chronology, route state, source status, and established details before writing.
- A character cannot act on information they have not learned.
- Distinguish known fact, inference, unconfirmed interpretation, allegation, and dramatized reconstruction.
- Evidence conflicts must be represented honestly rather than flattened into certainty.
- Authored dialogue is not rewritten merely for technical cleanup.
- Canon changes belong in the log below.

## Content boundaries

| Topic | Boundary |
| --- | --- |
| Homicide and human remains | May be discussed or strongly implied with a restrained content notice |
| Graphic gore / prolonged assault | Excluded by default; requires explicit future documentary-purpose decision |
| Criminal procedure details | Only what is necessary for narrative understanding; no instructional treatment |
| Victim dignity and surviving relatives | Mandatory consideration, especially for future real cases |
| Real-case allegations and disputed theories | Must be sourced, qualified, and never presented as settled fact without authority |
| Sexual violence, minors, hate crimes, suicide, and other sensitive topics | Treatment and rating remain TBD; require case-specific editorial review |

## Open canon questions

- Final project title
- Primary language and localization strategy
- Target rating and detailed content policy
- First researched real case and case-selection criteria
- Final world-map art and information architecture
- Production audio pipeline and public-release review of the prototype visual pipeline
- Public-release save-compatibility policy

## Reusable case outline template

- **Case status:** documented real case / clearly identified fictional composite
- **Location and period:** TBD
- **Authoritative sources and disputed facts:** TBD before real-case production
- **Victim-perspective purpose and ordinary details:** TBD
- **Incident threshold:** TBD, restrained by default
- **Discovery framing:** TBD
- **Evidence/timeline/contradictions:** TBD
- **Truth or current best reconstruction:** TBD
- **Legal/investigative outcome:** TBD
- **Victim memorial and emotional closure:** TBD
- **Media provenance by asset:** TBD

## Retcon / canon-change log

| Date | Decision | Previous canon | New canon | Affected content |
| --- | --- | --- | --- | --- |
| 2026-09-04 | Establish M1 product and prototype canon | Product/story fields were TBD | Documentary true-crime anthology model and fictional M1 case canon accepted | Story Bible, M1 implementation, roadmap/status/decisions |
| 2026-09-04 | Establish M1 visual canon and reconstruction label | M1 used abstract placeholders and visual identities were unspecified | Fictional identity references, 35mm documentary direction, and the `AI-GENERATED DRAMATIZED RECONSTRUCTION` label are canonical for M1 | Story Bible, M1 art, UI, provenance register |
