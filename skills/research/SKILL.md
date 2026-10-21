---
name: research
description: Investigate a question against primary sources and capture the findings as a durable file. Use when a decision depends on facts the team does not hold — library capabilities, API behaviour, standards, prior art.
---

# Research

Research exists so decisions rest on sources, not on what a model remembers.
The deliverable is a file the next phase can cite, not a chat answer that
evaporates.

## Process

1. **State the question and the decision it feeds.** Research without a
   decision attached wanders. Write both at the top of the file.
2. **Go to primary sources first:** official documentation, source code,
   standards, the vendor's own references. Secondary sources (articles,
   forum posts) may point to primaries; they never substitute for them.
3. **Capture claims with their sources.** Every load-bearing claim in the
   file carries its citation. Date-sensitive facts carry the date they were
   checked.
4. **List what remains unknown.** An honest open-questions section is part of
   the deliverable. Smoothing over a gap is fabrication.
5. **Write RESEARCH-<topic>.md** from `templates/research.md`. End with the
   implication for the decision: what the evidence supports, what it rules
   out, and what it leaves open.

## Rules

- Research is delegable: it is fact work, not decision work. The decision
  stays with the human and the orchestrator; the file carries the evidence.
- If sources conflict, report the conflict and which source outranks the
  other and why. Do not average them into a comfortable fiction.
- Stop when the decision can be made. Research that continues past its
  decision is procrastination with citations.

## Anti-patterns

- Citing a summary of a document instead of the document.
- Presenting search-result snippets as verified facts.
- Answering from training memory when the fact is checkable and the decision
  is expensive.
