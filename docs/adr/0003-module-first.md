# Title

Module-First Design

## Status

Accepted

## Date

2026-07-22

## Context

Long-lived systems become difficult to understand and change when responsibilities are diffuse and dependencies are accidental. A coherent unit of ownership and purpose helps contributors reason about change without needing complete knowledge of the entire system.

## Decision

Organize Orion around cohesive modules with clear responsibilities, intentional boundaries, and understandable relationships. Prefer changes that strengthen local ownership and reduce unnecessary coupling before introducing broader coordination.

## Consequences

Contributors must consider boundaries and ownership as part of design, not as a later cleanup task. Some duplication or deliberate separation may be preferable to premature consolidation. Module boundaries may evolve when evidence shows a clearer, more durable division of responsibility.

## Alternatives Considered

- Organize primarily around short-term tasks or individual preferences.
- Centralize unrelated responsibilities for apparent convenience.
- Defer boundary decisions until complexity has already accumulated.

## References

- [Project Orion Constitution](../ORION.md)
- [ADR System README](README.md)
