# Orion Engineering Handbook

## Welcome

Welcome to Project Orion. This handbook is a shared commitment to building software that earns confidence over time. It is written for every contributor: those making their first change, those maintaining established systems, and those who will inherit Orion decades from now.

Engineering at Orion is not only the act of producing working software. It is the stewardship of a system, its users, its history, and its future. Read this handbook before contributing, and use it to guide judgment when the right path is not obvious.

## Project Philosophy

Orion exists to create dependable software through deliberate, humane engineering. We value sustained usefulness over temporary novelty and clear responsibility over convenient ambiguity. Our work should remain understandable to people who were not present when it was created.

Every change participates in a larger whole. A local improvement that weakens trust, clarity, or maintainability is not progress. We build with respect for users, fellow contributors, and future stewards.

## Development Workflow

Begin with understanding. Read the relevant context, identify the user need, and clarify the expected outcome before changing the system. Prefer a small, well-scoped change over a broad change whose consequences are not understood.

Work in observable increments. Validate assumptions early, keep changes reviewable, and preserve a clear path to recovery when practical. When a decision is consequential or likely to be questioned later, record its reasoning in the appropriate durable documentation.

## Coding Standards

Write code for the next reader. Favor clear names, coherent responsibilities, explicit behavior, and straightforward control flow. Keep related concerns together and separate unrelated concerns. Avoid cleverness that obscures intent.

Code should make normal operation reliable and failure understandable. Handle expected failure modes deliberately, avoid silent loss of information, and make boundaries and assumptions visible. Apply consistency within a body of work, while improving confusing patterns when doing so is safe and justified.

## Documentation Standards

Documentation is part of the product and part of the engineering record. Document purpose, intent, constraints, and decisions that are not obvious from the work itself. Keep it accurate as the system changes; stale guidance is worse than absent guidance because it misleads with confidence.

Write for a capable contributor who lacks historical context. Explain why significant choices were made, not merely what exists. Preserve durable reasoning in records that future contributors can discover and trust.

## Testing Standards

Tests provide evidence, not ceremony. Every meaningful change should be evaluated in proportion to its risk, scope, and potential impact. Verify the expected behavior, relevant failure conditions, and the protection of existing commitments.

Keep tests independent, readable, and reliable. A test should communicate the behavior it protects and should not depend on incidental ordering, hidden state, or the results of other tests. When a defect is corrected, add focused evidence that prevents its return when practical.

## Commit Standards

Each commit is a durable statement of intent. Keep commits focused on one coherent purpose and ensure their message explains that purpose clearly. Do not mix unrelated cleanup, generated noise, or speculative changes with a meaningful decision unless their relationship is explicit.

A commit should leave the project in a sound state to the extent practical. It should be understandable on its own, supported by appropriate validation, and safe for another contributor to inspect or revert.

## Branching Strategy

Branches are temporary workspaces for deliberate change, not permanent silos. Keep them narrow in purpose, current with relevant shared work, and short-lived once their contribution has been integrated or intentionally set aside.

Use branch names and descriptions that communicate intent. Avoid parallel efforts that unknowingly alter the same responsibility in incompatible ways. When work becomes long-running or broadly consequential, make its ownership, goals, and decision points visible to the project.

## Pull Request Checklist

Before requesting review, confirm that:

- The change has a clear purpose and limited, understandable scope.
- Behavior has been validated in proportion to risk.
- Relevant documentation and decision records are accurate.
- Tests are independent and meaningful where testing is appropriate.
- Security, privacy, accessibility, reliability, and recovery concerns have been considered.
- The change does not include unrelated modifications.
- The description explains intent, notable tradeoffs, and any remaining limitations.

## Code Review Philosophy

Review is a collaborative practice for improving outcomes and sharing responsibility. It is not a contest, a formality, or a measure of personal worth. Reviewers should seek to understand intent, identify risks, protect project principles, and offer actionable feedback with respect.

Authors should welcome questions and challenge as opportunities to strengthen the work. Resolve disagreements through evidence, user impact, and Orion’s enduring principles. When a decision is made, record it when necessary and move forward together.

## Definition of Done

Work is done when it satisfies its intended outcome without compromising Orion’s trustworthiness or maintainability. It has been reviewed at an appropriate level, validated with suitable evidence, documented where future understanding requires it, and integrated without avoidable ambiguity.

Done does not mean perfect. It means the remaining limitations are known, acceptable, and visible to the people responsible for the system. Deferred work should be deliberate rather than accidental.

## Engineering Principles

### Build for trust.

Protect the confidence users place in Orion. Be accurate, transparent, careful with entrusted information, and honest about limitations. Never treat trust as a tradeoff to be spent for short-term convenience.

### Design for a century.

Choose clarity, durable reasoning, and responsible boundaries so future contributors can understand and evolve the system. Build for change without abandoning the commitments that make Orion recognizable and dependable.

### Improve with every commit.

Leave the project more understandable, reliable, or maintainable than you found it. Improvement may be small, but it should be intentional. Each contribution is an opportunity to reduce future uncertainty and strengthen the work for those who follow.
