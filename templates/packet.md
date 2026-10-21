# Packet: <ticket ID>

<!-- STABLE HEADER (byte-identical across this run): suite rules, repo
     layout, CONSTRAINTS.md floor, verdict vocabulary. -->

## Ticket
< ID and path. Read the ticket; it is the requirement. >

## Read first (pointers, in order)
< Spec sections, AC IDs, DESIGN.md / API.md / ERD.md paths, ADRs. >

## Scope
< The one coherent change. Files you may touch; files you must not touch. >

## Acceptance
< AC IDs to satisfy. Verification commands to run, copied from the ticket. >

## Report
Write the report to <path> in the fixed schema (templates/report.md).
Status vocabulary: DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED.
