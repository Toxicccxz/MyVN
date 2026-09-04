# Roadmap

## M0 — Repository and Ren'Py Foundation

**Status:** COMPLETE (engine-backed validation remained unavailable in the M0 environment).

Goals:

- Clean Ren'Py project
- Documents and local tooling
- Project launches
- Lint works
- Initial smoke-test foundation
- Stable baseline

The generated project baseline, repository structure, policy, documentation, and Windows scripts are in place. The limitation of the original validation environment remains recorded in project status history.

## M1 — Playable Vertical Slice

**Status:** IMPLEMENTATION COMPLETE; engine lint, automated testcase, and runtime verification blocked until `RENPY_SDK` is configured.

Target roughly 5–15 minutes. It must prove:

- Main menu → Start → story
- Background
- Character sprite/expression
- Dialogue and narration
- BGM and SFX
- Meaningful player choice
- State affected by the choice
- Branch/convergence or a small ending
- Save/load/rollback
- Automated story-flow test
- Runtime validation

## M2 — Visual/UI Baseline

After the vertical slice:

- Typography
- Dialogue/name box
- Choice UI
- Quick-menu decision
- Main-menu direction
- History/save/load/preferences styling
- Accessibility
- Reference resolution/layout rules

## M3 — Production Content Pipeline

- Sprite naming and variants
- Background/CG conventions
- Audio conventions
- Asset provenance
- Chapter-production rhythm
- Story Bible readiness

## M4 — Chapter Production

Scope intentionally remains open until real story scope and canon exist.

## M5 — Public Demo Release Gate

Eventually include:

- Release checklist
- Save-compatibility decision
- Clean Windows build
- Core-flow validation
- Placeholder cleanup
- Third-party asset provenance
- Versioning and known issues
