# Roadmap

## M0 — Repository and Ren'Py Foundation

**Status:** Foundation implemented; SDK-backed validation pending.

Goals:

- Clean Ren'Py project
- Documents and local tooling
- Project launches
- Lint works
- Initial smoke-test foundation
- Stable baseline

The generated project and its prior successful 8.5.3 launch evidence are preserved. Repository structure, policy, documentation, and scripts are in place. Current lint/test/runtime validation still requires a configured `RENPY_SDK`.

## M1 — Playable Vertical Slice

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

