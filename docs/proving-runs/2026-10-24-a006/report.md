# Proving run A-006 — copy pass audited against the copy.md fragments

Run: 2026-10-24. Subject: the complete user-facing copy of Linkstash
(`app/static/index.html` in ~/workspace/linkstash) — all 21 distinct
strings, extracted mechanically into `ui-strings.txt` in this folder
so the audit's coverage is checkable, not sampled.

## Criterion (from the A-006 record)

"a proving run that uses the fragments on real work — a design review
run with the click-through check, or a copy pass audited against the
new copy.md sections." This run takes the copy-pass route, and also
exercises the run's other vendored fragment, `scripts/contrast-check.py`,
on the project's real palette pairs (results filed in the A-005
report: 15.5:1, 6.2:1, 4.9:1, 6.5:1, all PASS).

## Audit, test by test (copy.md "Tells in the body of the copy")

| Test | Result across 21 strings |
| --- | --- |
| Actor tests | PASS, with one examined case: "Tautan yang sudah selesai dapat diarsipkan dari daftar aktif agar tidak memenuhi tampilan utama" is passive, but the actor is genuinely the user's own archiving act explained in an empty state — exactly the case "What not to flag" protects. Not flagged. |
| Forced rule of three | PASS. No triads anywhere; the empty states offer at most two suggestions ("kata kunci lain atau bersihkan pencarian"). |
| Negative parallelism | PASS. No "not just X, it's Y", no "no setup, no hassle" tails. |
| Synonym cycling | PASS, positively: one word per referent throughout — "tautan" in every state (aktif / tersimpan / diarsipkan), and one word per action on buttons (Simpan, Hapus, Batal, Ubah) including the delete confirmation reusing "Hapus" for the same action, which is the one-word-per-action rule working, not a duplication bug. |
| False ranges / aphorisms | PASS. No proverb-shaped lines; the longest string is a plain instruction. |
| Weasel attributions | PASS. No authority claims of any kind; the UI makes no marketing claims at all. |
| Speculative gap-filling | PASS. Nothing asserts an effect on the reader; even the count line ("0 tautan aktif") is a measured state, not a claim. |
| Banned opening lines | PASS (scope note: these are UI labels and empty states, not page openers; none matches the banned table's shapes). |

## Findings

1. Zero violations — and the audit can say why that is credible
   rather than lenient: the two candidate flags a naive pass would
   raise (the one passive sentence, the repeated "Hapus") are both
   explicitly protected by the "What not to flag" fragment, and the
   report records them as examined-and-cleared instead of silently
   passing. The false-positive discipline is the fragment under test,
   and it fired correctly in both directions: nothing flagged that
   should not be, and the near-misses are documented.
2. Scope honesty: Linkstash ships no marketing page, FAQ, or landing
   copy, so the FAQ/self-audit sections of copy.md had nothing to
   bite on. The criterion's copy-pass route is satisfied for the
   fragments that apply to real UI microcopy; the FAQ sections
   remain unexercised and this report does not pretend otherwise.

## Verdict

The fragments did real work on real copy: a complete-corpus audit
(not a sample), each tell applied as a test, and the what-not-to-flag
discipline demonstrably preventing the two false positives the corpus
offered. A-006 is ready to promote EXPOSED → ADAPTED.
