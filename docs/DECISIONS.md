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

