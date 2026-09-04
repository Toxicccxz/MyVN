# Decision Log

This file records durable accepted decisions, not a task journal.

## Decision template

### DNN — Title

- **Status:** Proposed / Accepted / Superseded
- **Date:** YYYY-MM-DD
- **Context:** What stable problem or constraint requires a decision?
- **Decision:** What is accepted?
- **Consequences:** What becomes easier, harder, required, or prohibited?
- **Supersedes / superseded by:** None, or decision ID

## D001 — Keep Ren'Py architecture lightweight

- **Status:** Accepted
- **Date:** 2026-09-04
- **Context:** Ren'Py already provides narrative flow, UI, serialization, input, audio, and rendering.
- **Decision:** Use Ren'Py script and built-ins by default; add only small explicit state/helpers and no Godot-style or enterprise application layering.
- **Consequences:** The project stays VN-focused. Larger Python/domain systems require a demonstrated gameplay need.
- **Supersedes / superseded by:** None

## D002 — Pin the initial engine to Ren'Py 8.5.3

- **Status:** Accepted
- **Date:** 2026-09-04
- **Context:** A stable supported engine makes local and automated validation reproducible.
- **Decision:** Ren'Py 8.5.3 is the supported engine until a dedicated upgrade task changes it.
- **Consequences:** SDK upgrades are explicit compatibility/validation work, not incidental changes.
- **Supersedes / superseded by:** None

## D003 — Keep `main` stable and use focused branches

- **Status:** Accepted
- **Date:** 2026-09-04
- **Context:** AI-assisted changes need reviewable scope without heavyweight ceremony.
- **Decision:** Treat `main` as the stable integration line and use focused branches for normal implementation.
- **Consequences:** Coherent features/chapters remain reviewable; merging and releases still require explicit authorization.
- **Supersedes / superseded by:** None

## D004 — Make the Story Bible canonical story authority

- **Status:** Accepted
- **Date:** 2026-09-04
- **Context:** Canon must remain consistent across many future authored and AI-assisted sessions.
- **Decision:** `docs/STORY_BIBLE.md` owns story, world, character, tone, and continuity facts.
- **Consequences:** Missing canon is reported or narrowly marked TBD rather than silently invented; authored canon changes are recorded.
- **Supersedes / superseded by:** None

## D005 — Use a dual-perspective case structure

- **Status:** Accepted
- **Date:** 2026-09-04
- **Context:** The anthology needs empathy before investigation and a repeatable dramatic form.
- **Decision:** The default case model follows the victim before the crime, then changes to a third-person investigation after the crime.
- **Consequences:** Earlier ordinary details can be reinterpreted as evidence; exact scene counts may vary without discarding the two-perspective model.
- **Supersedes / superseded by:** None

## D006 — Adopt a victim-first editorial principle

- **Status:** Accepted
- **Date:** 2026-09-04
- **Context:** True-crime presentation can reduce victims to objects of violence.
- **Decision:** “The victim is a person first and a case second.” Each completed case establishes ordinary life and provides person-centered closure.
- **Consequences:** Spectacle does not take priority over dignity, continuity, relationships, or human consequences.
- **Supersedes / superseded by:** None

## D007 — Keep violence presentation restrained

- **Status:** Accepted
- **Date:** 2026-09-04
- **Context:** Disturbing cases can be understood without gratuitous depiction.
- **Decision:** Graphic violence, prolonged assault recreation, and procedural killing detail are not the default language. Victim play normally ends at the incident threshold; discovery favors implication and aftermath.
- **Consequences:** Graphic material requires a later explicit decision with a clear documentary purpose.
- **Supersedes / superseded by:** None

## D008 — Prove the format with a fictional composite case

- **Status:** Accepted
- **Date:** 2026-09-04
- **Context:** The narrative and technical format should be validated before adapting real deaths.
- **Decision:** M1 uses only `The Red Umbrella`, an unmistakably fictional composite set in Toronto in October 1998. Real-case production requires prior research and provenance work.
- **Consequences:** No real victim, offender, or historical homicide is represented by M1, and no second case is introduced.
- **Supersedes / superseded by:** None

## D009 — Distinguish authentic and reconstructed media

- **Status:** Accepted
- **Date:** 2026-09-04
- **Context:** Documentary presentation must not manufacture false evidence or provenance.
- **Decision:** Authentic archival, recreated/dramatized, AI-generated reconstruction, and original game media remain explicitly distinguishable.
- **Consequences:** AI/recreated imagery cannot be presented as authentic archival, police, press, or crime-scene material; credits and case sources must preserve provenance.
- **Supersedes / superseded by:** None

## D010 — Favor interactive documentary over detective simulation

- **Status:** Accepted
- **Date:** 2026-09-04
- **Context:** Interaction should support narrative attention without requiring a police simulator or large systems architecture.
- **Decision:** Use light object, evidence, timeline, and interpretation interactions to increase presence, memory, pacing, and understanding.
- **Consequences:** Avoid unrelated minigames, complex inventory, forensic engines, omnipotent detective framing, and historical game-over puzzles.
- **Supersedes / superseded by:** None
