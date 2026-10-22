# Proving brief A-002 / 2 of 2 — component scope (verbatim)

> Komponen tunggal saja: form pendaftaran kelas seduh (nama, email,
> pilihan kelas, tombol daftar) sebagai satu komponen mandiri, bukan
> halaman. Tampilkan semua keadaan yang mungkin dialami pengguna.

## Why this brief stresses A-002 (orchestrator note, not part of the brief)

- Component-scope mode must fire: the page machinery (macrostructure,
  nav, footer, enrichment, preview block) stands down explicitly.
- The eight-state contract from ux-heuristics (absorbed from hallmark's
  interaction-and-states) becomes mandatory instead, and the deliverable
  is a forced-state preview rendering every state labelled.
- Input geometry rules must hold in CSS: border-width constant across
  states, a reserved outline slot so focus never shifts layout, input
  height equals button height.
