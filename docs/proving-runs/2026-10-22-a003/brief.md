# Proving brief A-003 (verbatim)

> Buat set figure untuk laporan praktikum klasifikasi Iris (150 baris,
> 3 spesies, 4 fitur numerik plus kolom spesies nominal yang ter-encode
> angka) dan hasil evaluasi 4 model yang semua akurasinya berhimpit di
> 92–99%. Figure harus menunjukkan (1) hubungan sepal dan petal antar
> spesies, (2) distribusi satu fitur per spesies, (3) hasil pembersihan
> data yang cacatnya kecil (duplikat dan missing hanya hitungan jari)
> dibanding total 150 baris, dan (4) perbandingan akurasi 4 model itu.
> Pembaca termasuk penyandang buta warna, figure akan dicetak dan juga
> dibaca di layar, dan setiap figure harus bisa dipahami tanpa
> mengandalkan warna saja. Jangan pakai pie, rainbow, atau sumbu batang
> yang dipotong.

## Why this brief stresses A-003 (orchestrator note, not part of the brief)

- The nominal `Species_Encoded` column is a trap: computing a Pearson
  correlation against it is meaningless. The run must refuse that move
  explicitly in its notes.
- Three species need a colourblind-safe categorical palette with a
  backup channel (distinct marker per species), per the colour rules.
- Small cleaning counts (single digits) plotted against a ~150 total
  on one axis get crushed; the composition rules require splitting or
  re-scaling the panel so the small counts stay readable.
- Model accuracies clustered at 92–99% tempt a bar chart with a
  truncated axis (a banned lie) or a full 0–100 bar chart where all
  bars look identical. The encoding rules point to a dot plot on an
  honestly marked scale.
- Every figure needs a title (what it is), a caption stating the
  takeaway (what to conclude), and a source line — plus a data-table /
  text-summary fallback for the accessibility gate.
- The four evaluation accuracies must be computed by actually training
  the four models on the dataset in the run script, never invented.
  Model choice is the worker's, recorded in the script and summary.
