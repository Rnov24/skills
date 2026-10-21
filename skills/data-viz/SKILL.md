---
name: data-viz
description: Design and build data visualizations that tell the truth — chart selection by question and perceptual accuracy, rendering technology by scale, established layout algorithms, and chart accessibility. Use for charts, graphs, dashboards, plots, and any data presentation surface.
phase: design
keywords: data-viz, chart, grafik, dashboard, visualisasi data, plot, diagram, sankey, heatmap, graph, statistik
---

# Data viz

A chart is an argument. Every encoding choice either makes the data easier
to read correctly or quietly lies on its behalf. This skill governs that
choice, for product dashboards and for research figures alike. It is a
discipline skill, not a phase: it is loaded by `design` when a surface
contains charts, and by whoever builds a figure, a report, or an analytics
view anywhere else in the workflow.

## The five questions, in order

Before any code, answer these. The answers are the design.

1. **What question does this chart answer?** One sentence. A chart that
   answers two questions answers neither; split it.
2. **What encoding carries the main comparison?** Chosen by perceptual
   accuracy, below.
3. **How much data?** Volume picks the rendering technology, below.
4. **Is there an established algorithm for this layout?** If yes, using it
   is mandatory. Graph layout, tree layout, treemaps, and spatial indexing
   are solved problems; a hand-rolled layout is a defect, not a craft flex.
5. **Can everyone read it?** Colour is never the only channel, and a data
   table or text summary exists as the fallback representation.

## Encoding by perceptual accuracy

Human judgement of visual channels is not equally accurate. The established
ranking, most accurate first: position on a common scale, position on
non-aligned scales, length, angle and slope, area, volume, and last colour
saturation and hue.

Consequences that follow from the ranking and are not negotiable:

- Comparisons belong on position or length. That is why bar charts beat pie
  charts (angle) which beat bubble charts (area) for comparing values.
- Colour encodes category or a low-to-high scale, never precise quantity.
- The channel must match the data type: quantitative data takes position,
  length, or area; ordinal data takes position, density, or saturation;
  categorical data takes shape, hue, or spatial region.
- Reserve the channels the eye catches pre-attentively — hue contrast,
  size, position outliers — for the one thing the chart exists to say.
  Everything popping means nothing pops.

## Chart selection by question

- Comparing values: bar chart.
- Change over time: line chart.
- Distribution: histogram or box plot.
- Relationship between two measures: scatter plot.
- Part to whole: stacked bar or treemap. A pie only when there are very
  few slices and the story is one dominant share.
- Connections and flows: network graph for relations, Sankey for flows
  with quantities.
- Hierarchy: tree or treemap; sunburst only when depth is shallow.
- Geography: choropleth for regional values, symbol map for point events.

Volume modifies the choice: under roughly 20 points, label directly and
skip legends; a few hundred points is the standard case; past a few
thousand, aggregation or filtering is part of the design, not an
optimisation added later.

## Rendering technology by scale

- Under about 1,000 elements: SVG. DOM events, crisp scaling, and screen
  reader semantics come free.
- Roughly 1,000 to 10,000: Canvas. Batch the drawing, plan hit-testing
  deliberately, animate with the frame loop.
- Over 10,000: WebGL-class rendering, or aggregate until the count falls.
  SVG with thousands of nodes is an implementation anti-pattern regardless
  of how the prototype felt.

Layout computation for large graphs runs off the main thread, hit-testing
uses a spatial index, and only the visible viewport is rendered. These are
defaults, not performance heroics.

Established libraries by job, chosen before anything custom is written:
layered DAG and flowchart layout (dagre, ELK), force-directed networks
(d3-force, Cytoscape), hierarchies and treemaps (d3-hierarchy), Sankey and
chord diagrams (the d3 modules), very large graphs (Sigma, deck.gl-class
WebGL). In Python and research contexts the same encoding rules apply to
matplotlib, Plotly, and Altair figures; the library changes, the
perceptual law does not.

## Colour for data

- Sequential scales run low to high in one hue family or a perceptually
  uniform ramp; diverging scales split at a meaningful midpoint; categorical
  palettes are hues of similar weight. Rainbow ramps are banned: their
  perceptual steps are uneven, so they invent bands the data does not have.
- In a product surface, chart colours come from the project's DESIGN.md
  tokens like everything else. A chart is not a licence to introduce a
  second palette. Where DESIGN.md has no data palette yet, add one there
  first, then chart from it.
- At most about seven to ten categorical colours before categories must be
  grouped, filtered, or faceted instead.
- Text contrast follows the suite floor (4.5:1, 3:1 for large text and UI
  components), and every colour encoding has a backup channel: shape,
  pattern, position, or a direct label.

## Composition and annotation

- Annotate the insight, not the data. The caption says what the reader
  should conclude; the title says what the chart is; the source line says
  where the data came from. All three exist.
- Callouts are rationed: one to three highlighted points, with reference
  lines for benchmarks, targets, or averages when they change the reading.
- Prefer direct labelling inside the chart over a separate legend when the
  series count allows it.
- Axes are labelled with units, ticks sit at meaningful intervals, and bar
  charts start at zero. A truncated axis on a bar chart is a lie with
  extra steps; if a line chart's axis must be truncated, the truncation is
  visibly marked.
- Aspect ratio is a choice with consequences (trend charts bank slopes
  toward roughly 45 degrees; scatter plots are near square when correlation
  is the story), never whatever the container happened to be.

## Interaction

For interactive charts the reading order is overview first, then zoom and
filter, then details on demand. Coordinated views brush and link rather
than updating in isolation, transitions between states are animated so the
reader can track what moved, and filtering is always reversible in one
obvious action. A dashboard composes its charts under one hierarchy: the
most important question gets the strongest position and the largest area,
related charts group, and the page reads in the audience's scan pattern,
not in the order the queries were written.

## Accessibility gate

A chart is not done until all of these hold:

- No information is carried by colour alone.
- Interactive elements are reachable and operable by keyboard, with data
  points traversable in a logical order.
- The graphic exposes a title and a description to assistive technology,
  and dynamic updates are announced politely.
- A data table or an equivalent text summary of the key insight exists as
  an alternative representation.
- The palette survives colour-vision deficiency, checked with a simulator
  or a known-safe ramp, not by optimism.

## Anti-patterns

Three-dimensional charts, pie charts past a handful of slices, dual axes
joining unrelated scales, non-zero bar baselines, rainbow ramps,
colour-only encodings, decoration that competes with the data, overplotting
left unaggregated, custom layout algorithms where a library exists,
thousands of SVG nodes, layout work on the main thread, and hit-testing
without a spatial index. Each of these has appeared in real work; each is
a review finding, not a style preference.

---
*Mechanisms in this skill were reimplemented in the suite's own words from
the data-visualization skill in NTCoding/claude-skillz (no licence file in
that repository, so no upstream text was copied), absorbed 2026-10-21.
Perceptual foundations after Cleveland & McGill (1984) and Shneiderman
(1996). Status: EXPOSED (A-003) until a proving run promotes it.*
