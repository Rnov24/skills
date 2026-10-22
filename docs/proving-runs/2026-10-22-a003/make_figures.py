#!/usr/bin/env python3
"""
Proving run A-003 — Iris figures following the rnov24 data-viz skill.

Reproducible: fixed seed, data from sklearn.datasets.load_iris only.
All numbers are computed from the real data at runtime; nothing is
hard-coded to match the brief's expectations.

Run with:
  ~/workspace/indoasag-env/bin/python make_figures.py
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

SEED = 42
OUT = Path(__file__).resolve().parent
DPI = 300

# Okabe-Ito colourblind-safe categorical palette (3 of 8 colours used).
# Recorded hexes — used identically in every figure:
#   setosa     #E69F00 (orange)
#   versicolor #56B4E9 (sky blue)
#   virginica  #009E73 (bluish green)
PALETTE = {
    "setosa": "#E69F00",
    "versicolor": "#56B4E9",
    "virginica": "#009E73",
}
# Backup channel: a distinct marker per species, so colour is never alone.
MARKERS = {
    "setosa": "o",
    "versicolor": "s",
    "virginica": "^",
}
SOURCE_LINE = "Source: sklearn.datasets.load_iris (Fisher 1936), loaded at runtime; n=150."

plt.rcParams.update({
    "figure.dpi": DPI,
    "savefig.dpi": DPI,
    "font.size": 9,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
})


def add_title_caption(fig, title, takeaway):
    fig.suptitle(title, fontsize=12, fontweight="bold", y=0.98)
    fig.text(0.5, 0.02, f"Takeaway: {takeaway}\n{SOURCE_LINE}",
             ha="center", va="bottom", fontsize=8, style="italic", wrap=True)


def main():
    iris = load_iris()
    feature_names = [n.replace(" (cm)", "").strip() for n in iris.feature_names]
    # columns: sepal length, sepal width, petal length, petal width — all in cm
    df = pd.DataFrame(iris.data, columns=feature_names)
    df["species"] = [iris.target_names[t] for t in iris.target]
    # Encoded nominal column, as named in the brief. It is used ONLY as a
    # categorical label for the cleaning panel bookkeeping — never as a
    # numeric variable. No correlation is computed against it (see summary.md).
    df["Species_Encoded"] = iris.target.astype(int)

    # --- Real cleaning numbers, computed as loaded ---
    duplicate_count = int(df.duplicated(subset=feature_names + ["species"]).sum())
    # duplicated() counts rows beyond the first occurrence.
    missing_count = int(df.isna().sum().sum())
    total_rows = int(len(df))
    print(f"total_rows={total_rows}")
    print(f"duplicate_rows_beyond_first={duplicate_count}")
    print(f"missing_values={missing_count}")

    # --- Real model accuracies on a fixed split ---
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=SEED, stratify=y
    )
    print(f"split=train_test_split(test_size=0.30, random_state={SEED}, stratify=y) "
          f"train={len(X_train)} test={len(X_test)}")
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=SEED),
        "k-NN (k=5)": KNeighborsClassifier(n_neighbors=5),
        "SVM (RBF)": SVC(kernel="rbf", random_state=SEED),
        "Random Forest": RandomForestClassifier(n_estimators=300, random_state=SEED),
    }
    accuracies = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        acc = float(accuracy_score(y_test, model.predict(X_test)))
        accuracies[name] = acc
        print(f"accuracy[{name}]={acc:.4f} ({acc*100:.2f}%)")

    # Data-table fallback for the scatter (full plotted data)
    df_out = df.copy()
    df_out.to_csv(OUT / "figures-data.csv", index=False)

    species = list(iris.target_names)

    # ============ Figure 1: sepal vs petal scatter by species ============
    fig, ax = plt.subplots(figsize=(7, 5.2))
    for sp in species:
        sub = df[df["species"] == sp]
        ax.scatter(sub["petal length"], sub["sepal length"],
                   c=PALETTE[sp], marker=MARKERS[sp], s=55,
                   edgecolors="black", linewidths=0.4, label=sp)
    ax.set_xlabel("Petal length (cm)")
    ax.set_ylabel("Sepal length (cm)")
    ax.legend(title="Species (colour + marker)", loc="upper left")
    ax.grid(True, alpha=0.25)
    add_title_caption(
        fig,
        "Figure 1 — Sepal length vs petal length by Iris species",
        "Setosa separates cleanly at short petals, while versicolor and virginica overlap in the middle range.")
    fig.tight_layout(rect=[0, 0.08, 1, 0.94])
    fig.savefig(OUT / "fig1_sepal_vs_petal_scatter.png", dpi=DPI)
    plt.close(fig)

    # ============ Figure 2: distribution of petal length by species ============
    fig, ax = plt.subplots(figsize=(7, 5.2))
    data_by_species = [df.loc[df["species"] == sp, "petal length"].values for sp in species]
    bp = ax.boxplot(data_by_species, patch_artist=True, tick_labels=species,
                    medianprops=dict(color="black", linewidth=1.2))
    for patch, sp in zip(bp["boxes"], species):
        patch.set_facecolor(PALETTE[sp])
        patch.set_alpha(0.55)
    # jittered raw points with species markers as a second channel
    rng = np.random.default_rng(SEED)
    for i, sp in enumerate(species, start=1):
        vals = df.loc[df["species"] == sp, "petal length"].values
        x = rng.normal(loc=i, scale=0.05, size=len(vals))
        ax.scatter(x, vals, c=PALETTE[sp], marker=MARKERS[sp], s=28,
                   edgecolors="black", linewidths=0.4, zorder=3)
    ax.set_ylabel("Petal length (cm)")
    ax.set_xlabel("Species")
    ax.grid(True, axis="y", alpha=0.25)
    add_title_caption(
        fig,
        "Figure 2 — Distribution of petal length by Iris species",
        "Petal length rises in steps from setosa to virginica, with versicolor bridging the other two.")
    fig.tight_layout(rect=[0, 0.08, 1, 0.94])
    fig.savefig(OUT / "fig2_petal_length_distribution.png", dpi=DPI)
    plt.close(fig)

    # ============ Figure 3: cleaning counts, split panel ============
    # One crushed axis would make the single-digit defects invisible next to
    # 150 total rows, so the total and the defects get separate panels with
    # their own honestly labelled scales. All bars start at zero.
    fig, axes = plt.subplots(1, 2, figsize=(7.5, 5.2),
                             gridspec_kw={"width_ratios": [1, 1.4]})
    ax0 = axes[0]
    ax0.bar(["Total rows"], [total_rows], color="#0072B2", edgecolor="black")
    ax0.set_ylim(0, max(10, total_rows * 1.15))
    ax0.set_ylabel("Count (rows)")
    ax0.set_title("Panel A — dataset size", fontsize=10)
    for i, v in enumerate([total_rows]):
        ax0.text(i, v + 3, str(v), ha="center", fontsize=10, fontweight="bold")
    ax0.grid(True, axis="y", alpha=0.25)

    ax1 = axes[1]
    defect_labels = ["Duplicate rows\n(beyond first)", "Missing values"]
    defect_values = [duplicate_count, missing_count]
    colours = ["#D55E00", "#CC79A7"]  # remaining Okabe-Ito hues
    ax1.bar(defect_labels, defect_values, color=colours, edgecolor="black")
    top = max(defect_values) if max(defect_values) > 0 else 1
    ax1.set_ylim(0, top * 1.35 + 0.5)
    # Counts take integer ticks only (review fix, 2026-10-22): the auto
    # ticks landed on 0.25 steps, which implies a precision counts lack.
    ax1.set_yticks(range(0, top + 2))
    ax1.set_ylabel("Count")
    ax1.set_title("Panel B — defects (own scale, starts at zero)", fontsize=10)
    for i, v in enumerate(defect_values):
        ax1.text(i, v + top * 0.06 + 0.1, str(v), ha="center", fontsize=10, fontweight="bold")
    ax1.grid(True, axis="y", alpha=0.25)

    add_title_caption(
        fig,
        "Figure 3 — Data-cleaning counts for the Iris dataset as loaded",
        "The dataset is essentially clean: defects are single-digit counts, shown on their own scale so they stay readable.")
    fig.tight_layout(rect=[0, 0.08, 1, 0.94])
    fig.savefig(OUT / "fig3_cleaning_counts.png", dpi=DPI)
    plt.close(fig)

    # ============ Figure 4: model accuracy dot plot ============
    fig, ax = plt.subplots(figsize=(7, 5.2))
    names = list(accuracies.keys())
    vals = [accuracies[n] * 100 for n in names]
    ypos = np.arange(len(names))
    ax.scatter(vals, ypos, s=110, c="#0072B2", edgecolors="black", linewidths=0.6, zorder=3)
    for x, y in zip(vals, ypos):
        ax.text(x + 0.4, y, f"{x:.1f}%", va="center", fontsize=9, fontweight="bold")
    ax.set_yticks(ypos)
    ax.set_yticklabels(names)
    ax.set_xlabel("Test accuracy (%)")
    # Narrowed position scale is legitimate for a dot plot (position, not
    # length) and is labelled in full with ticks every 2 points.
    ax.set_xlim(80, 102)
    ax.set_xticks(np.arange(80, 101, 2))
    ax.grid(True, axis="x", alpha=0.25)
    ax.invert_yaxis()
    add_title_caption(
        fig,
        "Figure 4 — Test accuracy of four classifiers on Iris (30% hold-out)",
        "All four models perform closely on this hold-out, so the ranking should not be over-read.")
    fig.tight_layout(rect=[0, 0.08, 1, 0.94])
    fig.savefig(OUT / "fig4_model_accuracy_dotplot.png", dpi=DPI)
    plt.close(fig)

    summary = {
        "total_rows": total_rows,
        "duplicate_rows_beyond_first": duplicate_count,
        "missing_values": missing_count,
        "split": "train_test_split(test_size=0.30, random_state=42, stratify=y); train=105, test=45",
        "accuracies": accuracies,
        "palette": PALETTE,
        "markers": MARKERS,
    }
    print(json.dumps(summary, indent=2))
    (OUT / "computed_numbers.json").write_text(json.dumps(summary, indent=2))
    print("figures written to", OUT)


if __name__ == "__main__":
    main()
