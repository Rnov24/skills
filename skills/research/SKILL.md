---
phase: discover
keywords: research, riset, cari tahu, documentation, dokumentasi, sources, fakta, compare, bandingkan, prior art
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

## Review mining

One research mode deserves its own discipline: mining what a product's
real users say about it (store reviews, G2/Capterra, Reddit, Hacker
News, the product's own request board) to find what they hate, what is
missing, and what is unsolved.

- **Never fabricate.** No invented reviews, quotes, counts, or sources.
  If a source cannot be reached, say so. If there are 14 reviews, the
  file says 14, with the sample size stated wherever a claim rests on
  them.
- **Every quote is verbatim and linked**, copied exactly with the URL of
  the review or thread. Reading, not scraping: read pages as a person
  does and copy rows into a CSV (`source,url,date,rating,text`); only
  official feeds and APIs within their terms are automated.
- **Rank with the tool, not by feel.** `python3 scripts/reviews.py
  reviews.csv` sorts the corpus into themes
  (`scripts/reviews-themes.json`, editable per category), weights low
  ratings and recency, and marks any theme under three reviews or from
  a single source as thin. Thin themes are reported as thin.
- Reviewers' words are research, never testimonials, and no fake
  reviews are ever created for or against any product.

The output feeds `define-product` as fix candidates and positioning
evidence inside the RESEARCH file, each item carrying its counts,
source spread, and linked quotes.

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
