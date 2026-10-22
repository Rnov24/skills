# Proving run A-003 — summary

All numbers below were computed at runtime by `make_figures.py` from
`sklearn.datasets.load_iris` (seed 42). Nothing was adjusted to fit the brief.

## Real computed numbers

- Total rows as loaded: **150**
- Duplicate rows (beyond the first occurrence, on the 4 features + species): **1**
- Missing values (all cells): **0**
- Split: `train_test_split(test_size=0.30, random_state=42, stratify=y)` — train 105, test 45

| Model | Test accuracy |
|---|---|
| Logistic Regression (`max_iter=1000`) | 0.9333 (93.33%) |
| k-NN (k=5) | 0.9778 (97.78%) |
| SVM (RBF kernel) | 0.9556 (95.56%) |
| Random Forest (300 trees) | 0.9111 (91.11%) |

Discrepancy against the brief: the brief expected all four accuracies to
cluster in 92–99%. Three do; Random Forest lands at 91.11%, just below that
band. The real value is plotted and reported as-is (see report.md, Concerns).

## Explicit refusal — correlation against `Species_Encoded`

No Pearson (or any) correlation was computed against the `Species_Encoded`
column, and none should be. Species is a **nominal** category: the integers
0/1/2 are arbitrary labels with no order, spacing, or magnitude. A correlation
coefficient against such codes measures the coding scheme, not the data, and
any value it returned would be meaningless. The column is used in the script
only as a categorical label. Relationships involving species are shown
instead by grouping (scatter coloured/shaped by species, box plots per
species), which is the correct treatment for a nominal variable.

---

## Figure 1 — `fig1_sepal_vs_petal_scatter.png`

Five questions:

1. **Question** — How do sepal length and petal length relate, and does that relationship differ by species?
2. **Encoding** — Position on two common scales (x = petal length in cm, y = sepal length in cm), the most accurate channel; species by Okabe-Ito hue **plus** a distinct marker per species.
3. **Volume** — 150 points, the standard case; plotted individually with no aggregation.
4. **Algorithm/library** — Direct scatter in matplotlib; no layout algorithm applies to a Cartesian scatter.
5. **Readability** — Colour is never alone (marker shapes differ), axes carry units (cm), and the full plotted data are in `figures-data.csv`.

Data-table fallback — per-species ranges and means (full 150-row data in `figures-data.csv`):

| Species | Sepal length min–max (cm) | Sepal mean (cm) | Petal length min–max (cm) | Petal mean (cm) | n |
|---|---|---|---|---|---|
| setosa | 4.3–5.8 | 5.006 | 1.0–1.9 | 1.462 | 50 |
| versicolor | 4.9–7.0 | 5.936 | 3.0–5.1 | 4.260 | 50 |
| virginica | 4.9–7.9 | 6.588 | 4.5–6.9 | 5.552 | 50 |

## Figure 2 — `fig2_petal_length_distribution.png`

Five questions:

1. **Question** — How is petal length distributed within each species, and how do the distributions compare?
2. **Encoding** — Position/length via box plots on a common cm scale, with jittered raw points overlaid so spread and sample size stay visible.
3. **Volume** — 150 values (50 per species); every raw point is shown, no binning choices to hide behind.
4. **Algorithm/library** — Standard matplotlib box plot (median, quartiles, 1.5×IQR whiskers); jitter uses a fixed-seed RNG (`default_rng(42)`), cosmetic only.
5. **Readability** — Species are separated by position on the x-axis (not colour alone), boxes also carry the species hue + marker shape, and the table below reproduces the distribution numerically.

Data-table fallback — petal length (cm) by species:

| Species | n | Mean | SD | Min | Q1 | Median | Q3 | Max |
|---|---|---|---|---|---|---|---|---|
| setosa | 50 | 1.462 | 0.174 | 1.0 | 1.40 | 1.50 | 1.575 | 1.9 |
| versicolor | 50 | 4.260 | 0.470 | 3.0 | 4.00 | 4.35 | 4.60 | 5.1 |
| virginica | 50 | 5.552 | 0.552 | 4.5 | 5.10 | 5.55 | 5.875 | 6.9 |

## Figure 3 — `fig3_cleaning_counts.png`

Five questions:

1. **Question** — How large is the dataset, and how many cleaning defects (duplicates, missing values) does it actually contain?
2. **Encoding** — Length (bars), with every bar starting at zero; the comparison that matters (defect vs defect) shares one scale in Panel B.
3. **Volume** — Three counts total; each is labelled directly with its value, so no legend or axis reading is required.
4. **Algorithm/library** — Plain matplotlib bar charts; counts computed with `pandas.DataFrame.duplicated` and `isna().sum()`.
5. **Readability** — The 150-row total and the single-digit defects are in **separate panels with their own labelled scales**, so the defects are not crushed against 150; values are printed on the bars and repeated in the table below.

Data-table fallback:

| Quantity | Count |
|---|---|
| Total rows | 150 |
| Duplicate rows (beyond first) | 1 |
| Missing values | 0 |

## Figure 4 — `fig4_model_accuracy_dotplot.png`

Five questions:

1. **Question** — How do the test accuracies of the four classifiers compare on the same hold-out split?
2. **Encoding** — Position on a common scale (dot plot), not length: that is what permits a narrowed 80–102% axis without lying, since no bar baseline is truncated; every dot is labelled with its exact value.
3. **Volume** — Four values; labelled directly, no legend.
4. **Algorithm/library** — matplotlib scatter (dot plot); accuracies from `sklearn.metrics.accuracy_score` on the fixed split above.
5. **Readability** — Model names are text on the y-axis and values are printed next to each dot, so the figure is fully readable in greyscale/print with no colour information at all.

Data-table fallback:

| Model | Test accuracy |
|---|---|
| Logistic Regression | 93.33% |
| k-NN (k=5) | 97.78% |
| SVM (RBF) | 95.56% |
| Random Forest | 91.11% |

---

## Accessibility-gate checklist (with evidence)

- **No information carried by colour alone** — Evidence: species use a backup channel in every species figure: distinct markers (setosa = circle `o`, versicolor = square `s`, virginica = triangle `^`) in Figures 1–2, plus species names as x-axis text in Figure 2. Figure 4 uses no colour encoding at all (model = y-axis text, value = printed label).
- **Palette survives colour-vision deficiency** — Evidence: the Okabe-Ito palette, designed for colour-vision deficiency. Species hexes used consistently across all figures: setosa `#E69F00`, versicolor `#56B4E9`, virginica `#009E73`. Figures 3–4 draw their non-species colours from the same Okabe-Ito family (`#0072B2` blue, `#D55E00` vermillion, `#CC79A7` reddish purple). No rainbow/jet colormap anywhere; no pie chart anywhere.
- **Title and description available** — Evidence: every PNG carries inside the image a title stating what the chart is, a one-sentence takeaway caption stating what to conclude, and a source line (`sklearn.datasets.load_iris (Fisher 1936), loaded at runtime; n=150`).
- **Data table / text summary fallback exists** — Evidence: the per-figure markdown tables above give every plotted aggregate; the full scatter data are in `figures-data.csv` (150 rows, the exact values plotted in Figures 1–2).
- **Print readability** — Evidence: all figures exported at 300 dpi; bars start at zero (Figure 3, both panels); units (cm) on all measurement axes (Figures 1–2).
- **Keyboard / screen-reader items** — Not applicable to static PNGs; the fallback representations above (tables + CSV) are the accessible alternative for these static figures.
