# Artifact registry

Every artifact the suite produces, in one place. An artifact may be created
only when its trigger fires. Each entry names the template in `templates/`,
the owning skill, the usual location inside a project repo, who consumes it,
and the gate that accepts it.

## Product artifacts

### BRIEF.md
- Trigger: any request bigger than a one-line fix, or any request whose real
  problem is not yet stated.
- Owner: `brief`. Template: `templates/brief.md`. Location: `docs/`.
- Consumers: research, grill, define-product.
- Gate: human approves problem, scope, and non-goals.

### RESEARCH-<topic>.md
- Trigger: a decision depends on facts the team does not already hold.
- Owner: `research`. Template: `templates/research.md`. Location: `docs/research/`.
- Consumers: brief, grill, spec.
- Gate: every load-bearing claim cites a primary source; unknowns are listed
  as unknowns, not smoothed over.

### ADR-<nnnn>-<slug>.md
- Trigger: a decision passes the three-gate test — hard to reverse, surprising
  without context, and the result of a real trade-off.
- Owner: `grill` (or any phase that resolves such a decision).
  Template: `templates/adr.md`. Location: `docs/adr/`.
- Consumers: spec, implement, future maintainers.
- Gate: written the moment the decision resolves, in the same session.

### GLOSSARY.md
- Trigger: a term is used with a project-specific meaning, or two people (or
  agents) use one word for two things.
- Owner: `grill` / `model`. Template: `templates/glossary.md`.
  Location: repo root or `docs/`.
- Consumers: everyone. One meaning per term, enforced on sight.

### PRD.md
- Trigger: a new product, or a feature with users, behaviour choices, and a
  success measure.
- Owner: `define-product`. Template: `templates/prd.md`. Location: `docs/`.
- Consumers: design, model, spec.
- Gate: human approves; problem, metrics with baselines and targets, scope
  and non-goals all present; unknowns marked TBD, never invented.

### PERSONAS.md
- Trigger: the PRD names more than one kind of user, or design decisions
  depend on who the user is.
- Owner: `define-product`. Template: `templates/persona.md`.
- Consumers: design (flows are written per persona), stories.
- Gate: each persona has goals, constraints, and a failure mode; no demographic
  decoration without behavioural consequence.

### STORIES.md
- Trigger: a PRD exists, or behaviour must be specified precisely enough to
  test.
- Owner: `define-product`. Template: `templates/stories.md`.
- Consumers: spec, tickets, review.
- Gate: every story has at least one acceptance criterion written in a
  checkable format (Given/When/Then or a measurable condition), and an ID.

## Design artifacts

### DESIGN.md
- Trigger: any user-facing surface is being built or changed beyond a trivial
  fix.
- Owner: `design`. Template: `templates/design.md`. Location: repo root.
- Consumers: implement (every UI worker reads it), review (design axis).
- Gate: tokens, typography, layout rules, component rules, motion rules, and
  explicit bans are written as checkable rules, not adjectives.

### USERFLOW.md
- Trigger: a feature spans more than one screen or state, or a persona's path
  can fail in more than one place.
- Owner: `design`. Template: `templates/userflow.md`.
- Consumers: spec, tickets, tests.
- Gate: every flow names its entry, happy path, failure paths, and exit state;
  every screen in a flow exists in DESIGN.md or is listed as new.

### Keyframes / references
- Trigger: a new visual direction, or a redesign of an existing surface.
- Owner: `design`. Location: `docs/design/keyframes/`.
- Gate: human approves the keyframe before implementation starts. Aesthetic
  bets are never committed unapproved.

## Technical artifacts

### DOMAIN.md
- Trigger: the project has entities with lifecycles, invariants, or rules
  that live outside any single screen or endpoint.
- Owner: `model`. Template: `templates/domain.md`.
- Consumers: ERD, API, spec.
- Gate: every entity has invariants; every rule names the entity it constrains.

### ERD.md
- Trigger: data is persisted, or an existing schema changes.
- Owner: `model`. Template: `templates/erd.md`.
- Consumers: API, tickets (migrations become their own tickets).
- Gate: every table traces to a domain entity; every relationship has
  cardinality and a deletion rule.

### API.md
- Trigger: a boundary exists that another system, client, or team consumes —
  HTTP API, library interface, CLI contract.
- Owner: `model`. Template: `templates/api.md`.
- Consumers: spec, implement, tests.
- Gate: every endpoint/operation has inputs, outputs, errors, and an auth
  rule; breaking-change policy stated once, up front.

### SPEC.md
- Trigger: work is handed to implementers (human or agent) as one unit.
- Owner: `spec`. Template: `templates/spec.md`.
- Consumers: tickets.
- Gate: spec cites story IDs, names its test seams, and lists open questions
  as answered or parked.

### tickets/*.md
- Trigger: a spec (or a plan too big for one session) is ready to execute.
- Owner: `tickets`. Template: `templates/ticket.md`.
  Location: `docs/tickets/` or the project tracker.
- Consumers: orchestrate, implement.
- Gate: each ticket declares what it covers (spec sections, AC IDs), its
  blocking edges, its files, and its verification commands. The unblocked
  frontier is the only legal parallel schedule.

### CONSTRAINTS.md
- Trigger: set up once per repo; amended whenever a quality incident teaches a
  new floor.
- Owner: `setup-workspace`. Template: `templates/constraints.md`.
- Consumers: verify, review.
- Gate: every dimension has a rule, a `Checked by` command, and a `Runs at`
  stage. The floor may only rise.

## Run artifacts

### PACKET-<ticket>.md and REPORT-<ticket>.md
- Trigger: any delegated unit of work.
- Owner: `orchestrate`. Templates: `templates/packet.md`,
  `templates/report.md`. Location: `.work/` (not committed) or the run folder.
- Gate: a packet with no report, or a report without evidence, is unfinished
  work, not completed work.

### REVIEW.md
- Trigger: an implement phase completes, or a risky decision needs a blind
  check.
- Owner: `review`. Template: `templates/review.md`.
- Gate: verdicts recorded per AC ID; Critical findings are fixed or parked
  with a written ruling, never silently dropped.

### RETRO.md
- Trigger: a feature ships, a run fails, or a loop hits its cap.
- Owner: `retro`. Template: `templates/retro.md`.
- Gate: each lesson names where it is filed so the next run reads it.

### Absorb report
- Trigger: a `/gluttony` run against an external skill repository.
- Owner: `gluttony`. Template: `templates/absorb-report.md`.
  Location: `docs/audit/absorbed/<date>-<repo>.md`.
- Gate: human approves the verdict summary and the diff before any absorbed
  unit is committed.

### ADAPTATIONS.md (the wheel)
- Trigger: a signal the `adapt` skill recognises — an escape, a rework hot
  spot, a finder miss, a repeated human correction, a recurring ruling, or
  a gluttony absorption awaiting promotion.
- Owner: `adapt`. Template: `templates/adaptation.md`.
  Location: `docs/ADAPTATIONS.md` of the suite itself.
- Gate: human approves each candidate before it is applied; rejected and
  reverted entries stay in the log with their reasons.
