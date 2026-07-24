# Architecture Decision Records

Architecture Decision Records (ADRs) preserve the reasoning behind consequential, long-lived decisions in Project Orion. They are permanent engineering records: a later decision may supersede an ADR, but the original record must remain available so contributors can understand the context, tradeoffs, and intent that shaped the project.

## Purpose

Use an ADR when a decision materially affects Orion’s principles, boundaries, operating model, or long-term direction. An ADR records what was decided, why it was decided, what follows from it, and which credible alternatives were considered. It does not need to describe implementation mechanics.

## Format and Naming

ADRs are stored in this directory and named with a zero-padded sequence number and a concise, lowercase title:

`NNNN-short-decision-title.md`

Each ADR uses these sections:

- Title
- Status
- Date
- Context
- Decision
- Consequences
- Alternatives Considered
- References

## Status Values

- **Proposed** — Under consideration and not yet a governing decision.
- **Accepted** — Adopted as the current decision and expected to guide future work.
- **Superseded** — Replaced by a newer ADR; retained as historical context.
- **Deprecated** — No longer recommended or applicable, without being directly replaced.
- **Rejected** — Considered and deliberately not adopted; retained to preserve the reasoning.

## Stewardship

ADRs are concise, evidence-based, and written for future contributors. Do not rewrite history to make prior decisions appear inevitable. When circumstances change, create a new ADR and link it to the earlier record. The goal is a durable record of responsible engineering judgment.
