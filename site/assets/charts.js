import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7.9.0/+esm";


const FALLBACK_COLOR = "#8a96a8";
const INK = "#172033";
const MUTED = "#697386";
const LINE = "#dfe5ec";
const SURFACE = "#f6f8fb";
const PAPER = "#ffffff";
const TEAL = "#4c9d96";
const VENUE_DOMAIN_COLORS = new Map([
  ["Artificial Intelligence", "#4c9d96"],
  ["Machine Learning", "#66add0"],
  ["Natural Language Processing", "#718dca"],
  ["Computer Vision", "#8296c7"],
  ["Graphics and Visualization", "#9380c1"],
  ["Human-Computer Interaction", "#b777a7"],
  ["Data Mining and Information Retrieval", "#a7719b"],
  ["Software Engineering", "#c47f91"],
  ["Systems & Hardware", "#d89368"],
  ["Multimodal & Audio", "#6f9fb2"],
  ["Interdisciplinary & General Science", "#8a96a8"],
]);

const VENUE_DOMAIN_LABELS = new Map([
  ["Artificial Intelligence", "AI"],
  ["Machine Learning", "ML"],
  ["Natural Language Processing", "NLP"],
  ["Computer Vision", "CV"],
  ["Graphics and Visualization", "Graphics & Vis."],
  ["Human-Computer Interaction", "HCI"],
  ["Data Mining and Information Retrieval", "Data Mining & IR"],
  ["Software Engineering", "Software Eng."],
  ["Systems & Hardware", "Systems & Hardware"],
  ["Multimodal & Audio", "Multimodal & Audio"],
  ["Interdisciplinary & General Science", "Interdisciplinary"],
]);

const tooltip = d3
  .select(document.body)
  .append("div")
  .attr("class", "chart-tooltip")
  .attr("role", "status")
  .attr("aria-live", "polite");

function format(value) {
  return d3.format(",")(value);
}

function share(value, total) {
  return d3.format(".1%")(value / total);
}

function showTooltip(event, title, detail) {
  tooltip
    .html(`<strong>${title}</strong><span>${detail}</span>`)
    .classed("is-visible", true);
  moveTooltip(event);
}

function moveTooltip(event) {
  const width = tooltip.node().offsetWidth;
  const left = Math.min(event.clientX + 16, window.innerWidth - width - 12);
  tooltip.style("left", `${Math.max(12, left)}px`).style("top", `${event.clientY + 16}px`);
}

function hideTooltip() {
  tooltip.classed("is-visible", false);
}

function createSvg(containerSelector, width, height, title, description) {
  const container = document.querySelector(containerSelector);
  if (!container) return null;
  const svg = d3
    .create("svg")
    .attr("class", "d3-svg")
    .attr("viewBox", `0 0 ${width} ${height}`)
    .attr("role", "img")
    .attr("aria-label", `${title}. ${description}`);
  svg.append("title").text(title);
  svg.append("desc").text(description);
  container.replaceChildren(svg.node());
  return svg;
}

function addGrid(svg, scale, ticks, x1, x2) {
  svg
    .append("g")
    .attr("class", "chart-grid")
    .selectAll("line")
    .data(scale.ticks(ticks))
    .join("line")
    .attr("x1", x1)
    .attr("x2", x2)
    .attr("y1", (value) => scale(value))
    .attr("y2", (value) => scale(value));
}

function drawHeroFamilies(catalog) {
  const width = 760;
  const height = 430;
  const margin = { top: 42, right: 64, bottom: 34, left: 222 };
  const familyTotal = d3.sum(catalog.families, (family) => family.count);
  const applicationOnly = catalog.summary.total - familyTotal;
  const data = catalog.families.map((family) => ({ ...family }));
  if (applicationOnly) {
    data.push({ name: "Application-only", count: applicationOnly, color: FALLBACK_COLOR });
  }

  const svg = createSvg(
    "#hero-family-chart",
    width,
    height,
    "Artifact family distribution",
    "Horizontal bars compare paper counts across six artifact families and application-only records.",
  );
  if (!svg) return;

  const x = d3
    .scaleLinear()
    .domain([0, d3.max(data, (item) => item.count)])
    .nice()
    .range([margin.left, width - margin.right]);
  const y = d3
    .scaleBand()
    .domain(data.map((item) => item.name))
    .range([margin.top, height - margin.bottom])
    .padding(0.34);

  svg
    .append("g")
    .attr("class", "chart-grid vertical-grid")
    .selectAll("line")
    .data(x.ticks(4))
    .join("line")
    .attr("x1", (value) => x(value))
    .attr("x2", (value) => x(value))
    .attr("y1", margin.top - 14)
    .attr("y2", height - margin.bottom + 7);

  svg
    .append("g")
    .attr("class", "chart-axis chart-axis-top")
    .attr("transform", `translate(0,${margin.top - 14})`)
    .call(d3.axisTop(x).ticks(4).tickSize(0));

  const rows = svg
    .append("g")
    .selectAll("g")
    .data(data)
    .join("g")
    .attr("class", "hero-bar-row")
    .on("pointerenter", (event, item) =>
      showTooltip(
        event,
        item.name,
        `${format(item.count)} papers, ${share(item.count, catalog.summary.total)} of the catalog`,
      ),
    )
    .on("pointermove", moveTooltip)
    .on("pointerleave", hideTooltip);

  rows
    .append("text")
    .attr("class", "chart-category")
    .attr("x", margin.left - 16)
    .attr("y", (item) => y(item.name) + y.bandwidth() / 2 + 5)
    .attr("text-anchor", "end")
    .text((item) => item.name);

  rows
    .append("rect")
    .attr("x", margin.left)
    .attr("y", (item) => y(item.name))
    .attr("width", (item) => Math.max(2, x(item.count) - margin.left))
    .attr("height", y.bandwidth())
    .attr("fill", (item) => item.color);

  rows
    .append("text")
    .attr("class", "chart-value")
    .attr("x", (item) => x(item.count) + 10)
    .attr("y", (item) => y(item.name) + y.bandwidth() / 2 + 5)
    .text((item) => item.count);
}

function drawComposition(catalog) {
  const width = 1160;
  const height = 650;
  const center = { x: 340, y: 330 };
  const familyTotal = d3.sum(catalog.families, (family) => family.count);
  const applicationOnly = catalog.summary.total - familyTotal;
  const families = catalog.families.map((family) => ({ ...family }));
  if (applicationOnly) {
    families.push({
      name: "Application-only",
      count: applicationOnly,
      color: FALLBACK_COLOR,
      types: [],
    });
  }
  const outerData = [];
  catalog.families.forEach((family) => {
    const typed = d3.sum(family.types, (type) => type.count);
    family.types
      .filter((type) => type.count)
      .forEach((type) => outerData.push({ ...type, family: family.name, color: family.color }));
    if (family.count > typed) {
      outerData.push({
        name: "Family-level",
        family: family.name,
        count: family.count - typed,
        color: family.color,
      });
    }
  });
  if (applicationOnly) {
    outerData.push({
      name: "Application-only",
      family: "Application-only",
      count: applicationOnly,
      color: FALLBACK_COLOR,
    });
  }

  const svg = createSvg(
    "#composition-chart",
    width,
    height,
    "Artifact taxonomy composition",
    "A two-level radial chart shows artifact families in the inner ring and artifact types in the outer ring.",
  );
  if (!svg) return;

  const familyPie = d3.pie().sort(null).value((item) => item.count)(families);
  const typePie = d3.pie().sort(null).value((item) => item.count)(outerData);
  const familyArc = d3.arc().innerRadius(108).outerRadius(184);
  const typeArc = d3.arc().innerRadius(190).outerRadius(255);
  const chart = svg.append("g").attr("transform", `translate(${center.x},${center.y})`);

  chart
    .selectAll("path.family-arc")
    .data(familyPie)
    .join("path")
    .attr("class", "family-arc")
    .attr("d", familyArc)
    .attr("fill", (item) => item.data.color)
    .attr("stroke", PAPER)
    .attr("stroke-width", 3)
    .on("pointerenter", (event, item) =>
      showTooltip(
        event,
        item.data.name,
        `${format(item.data.count)} papers, ${share(item.data.count, catalog.summary.total)}`,
      ),
    )
    .on("pointermove", moveTooltip)
    .on("pointerleave", hideTooltip);

  chart
    .selectAll("path.type-arc")
    .data(typePie)
    .join("path")
    .attr("class", "type-arc")
    .attr("d", typeArc)
    .attr("fill", (item) => item.data.color)
    .attr("fill-opacity", (item, index) => 0.38 + (index % 3) * 0.18)
    .attr("stroke", PAPER)
    .attr("stroke-width", 3)
    .on("pointerenter", (event, item) =>
      showTooltip(
        event,
        `${item.data.family}: ${item.data.name}`,
        `${format(item.data.count)} papers, ${share(item.data.count, catalog.summary.total)}`,
      ),
    )
    .on("pointermove", moveTooltip)
    .on("pointerleave", hideTooltip);

  chart
    .append("text")
    .attr("class", "chart-total")
    .attr("text-anchor", "middle")
    .attr("y", -2)
    .text(format(catalog.summary.total));
  chart
    .append("text")
    .attr("class", "chart-total-label")
    .attr("text-anchor", "middle")
    .attr("y", 25)
    .text("catalog papers");

  const legend = svg
    .append("g")
    .attr("class", "chart-legend")
    .attr("transform", "translate(665,85)");
  const legendRows = legend
    .selectAll("g")
    .data(families)
    .join("g")
    .attr("transform", (_, index) => `translate(0,${index * 76})`);
  legendRows
    .append("rect")
    .attr("width", 10)
    .attr("height", 38)
    .attr("fill", (item) => item.color);
  legendRows
    .append("text")
    .attr("class", "legend-title")
    .attr("x", 24)
    .attr("y", 13)
    .text((item) => `${item.name}  ${item.count}`);
  legendRows
    .append("text")
    .attr("class", "legend-detail")
    .attr("x", 24)
    .attr("y", 34)
    .text((item) => {
      const types = item.types.filter((type) => type.count).map((type) => type.name);
      return types.length ? types.join(" / ") : share(item.count, catalog.summary.total);
    });
}

function drawTrend(catalog) {
  const width = 960;
  const height = 610;
  const margin = { top: 118, right: 34, bottom: 68, left: 68 };
  const familyNames = catalog.families.map((family) => family.name);
  const color = new Map(catalog.families.map((family) => [family.name, family.color]));
  const years = [...new Set(catalog.papers.map((paper) => paper.year))].sort();
  const byYear = years.map((year) => {
    const row = { year };
    familyNames.forEach((family) => {
      row[family] = catalog.papers.filter(
        (paper) => paper.year === year && paper.artifact_family === family,
      ).length;
    });
    return row;
  });
  const series = d3.stack().keys(familyNames)(byYear);
  const maximum = d3.max(byYear, (row) => d3.sum(familyNames, (family) => row[family]));

  const svg = createSvg(
    "#trend-chart",
    width,
    height,
    "Artifact family growth",
    "Stacked bars compare annual paper counts for six artifact families.",
  );
  if (!svg) return;
  const x = d3
    .scaleBand()
    .domain(years)
    .range([margin.left, width - margin.right])
    .padding(0.34);
  const y = d3
    .scaleLinear()
    .domain([0, maximum])
    .nice()
    .range([height - margin.bottom, margin.top]);

  addGrid(svg, y, 5, margin.left, width - margin.right);
  svg
    .append("g")
    .attr("class", "chart-axis")
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).tickSize(0).tickPadding(14));
  svg
    .append("g")
    .attr("class", "chart-axis")
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y).ticks(5).tickSize(0).tickPadding(12));

  svg
    .append("g")
    .selectAll("g")
    .data(series)
    .join("g")
    .attr("fill", (layer) => color.get(layer.key))
    .selectAll("rect")
    .data((layer) => layer.map((item) => ({ item, family: layer.key })))
    .join("rect")
    .attr("x", ({ item }) => x(item.data.year))
    .attr("y", ({ item }) => y(item[1]))
    .attr("height", ({ item }) => Math.max(0, y(item[0]) - y(item[1])))
    .attr("width", x.bandwidth())
    .attr("stroke", PAPER)
    .attr("stroke-width", 1.5)
    .on("pointerenter", (event, { item, family }) => {
      const count = item[1] - item[0];
      showTooltip(event, `${item.data.year}: ${family}`, `${format(count)} papers`);
    })
    .on("pointermove", moveTooltip)
    .on("pointerleave", hideTooltip);

  svg
    .append("g")
    .selectAll("text")
    .data(byYear)
    .join("text")
    .attr("class", "chart-value")
    .attr("x", (row) => x(row.year) + x.bandwidth() / 2)
    .attr("y", (row) => y(d3.sum(familyNames, (family) => row[family])) - 12)
    .attr("text-anchor", "middle")
    .text((row) => d3.sum(familyNames, (family) => row[family]));

  const legend = svg.append("g").attr("class", "inline-legend");
  const legendItem = legend
    .selectAll("g")
    .data(catalog.families)
    .join("g")
    .attr("transform", (_, index) => `translate(${margin.left + (index % 3) * 290},${34 + Math.floor(index / 3) * 32})`);
  legendItem.append("rect").attr("width", 12).attr("height", 12).attr("fill", (item) => item.color);
  legendItem
    .append("text")
    .attr("class", "legend-title")
    .attr("x", 21)
    .attr("y", 11)
    .text((item) => item.name);
}

function drawVenues(catalog) {
  const width = 1000;
  const height = 650;
  const venues = catalog.publication_venues || [];
  const domainGroups = d3
    .groups(venues, (venue) => venue.domain)
    .map(([name, children]) => ({ name, children }));
  const accessibleCounts = venues
    .map((venue) => `${venue.name}, ${format(venue.count)}, ${venue.domain}`)
    .join("; ");

  const svg = createSvg(
    "#venue-chart",
    width,
    height,
    "Publication venue distribution",
    `A nested treemap compares published paper counts across normalized parent venues. Rectangle area shows paper count and color shows research area. Counts: ${accessibleCounts}.`,
  );
  if (!svg || !venues.length) return;

  const root = d3
    .hierarchy({ name: "Publication venues", children: domainGroups })
    .sum((node) => node.count || 0)
    .sort(
      (left, right) =>
        right.value - left.value || left.data.name.localeCompare(right.data.name),
    );
  d3
    .treemap()
    .size([width, height])
    .paddingOuter(8)
    .paddingInner(3)
    .paddingTop((node) => (node.depth === 1 ? 30 : 0))
    .round(true)(root);

  const domains = svg
    .append("g")
    .attr("class", "treemap-domains")
    .selectAll("g")
    .data(root.children || [])
    .join("g");

  domains
    .append("rect")
    .attr("class", "treemap-domain-frame")
    .attr("x", (domain) => domain.x0)
    .attr("y", (domain) => domain.y0)
    .attr("width", (domain) => domain.x1 - domain.x0)
    .attr("height", (domain) => domain.y1 - domain.y0)
    .attr("fill", (domain) => VENUE_DOMAIN_COLORS.get(domain.data.name) || FALLBACK_COLOR)
    .attr("stroke", (domain) => VENUE_DOMAIN_COLORS.get(domain.data.name) || FALLBACK_COLOR);

  domains
    .filter((domain) => domain.x1 - domain.x0 >= 58 && domain.y1 - domain.y0 >= 36)
    .append("text")
    .attr("class", "treemap-domain-label")
    .attr("x", (domain) => domain.x0 + 9)
    .attr("y", (domain) => domain.y0 + 19)
    .text((domain) => VENUE_DOMAIN_LABELS.get(domain.data.name) || domain.data.name);

  domains
    .filter((domain) => {
      const label = VENUE_DOMAIN_LABELS.get(domain.data.name) || domain.data.name;
      const requiredWidth = label.length * 7 + format(domain.value).length * 7 + 34;
      return domain.x1 - domain.x0 >= requiredWidth && domain.y1 - domain.y0 >= 36;
    })
    .append("text")
    .attr("class", "treemap-domain-total")
    .attr("x", (domain) => domain.x1 - 9)
    .attr("y", (domain) => domain.y0 + 19)
    .attr("text-anchor", "end")
    .text((domain) => format(domain.value));

  const venueLeaves = root.leaves();
  venueLeaves.forEach((leaf, index) => {
    leaf.clipId = `venue-tile-clip-${index}`;
  });
  const leaves = svg
    .append("g")
    .attr("class", "treemap-leaves")
    .selectAll("g")
    .data(venueLeaves)
    .join("g")
    .attr("class", "treemap-leaf")
    .on("pointerenter", (event, leaf) =>
      showTooltip(
        event,
        leaf.data.name,
        `${format(leaf.value)} published papers, ${share(leaf.value, catalog.summary.published)} of published papers, ${leaf.data.domain}`,
      ),
    )
    .on("pointermove", moveTooltip)
    .on("pointerleave", hideTooltip);

  leaves
    .append("clipPath")
    .attr("id", (leaf) => leaf.clipId)
    .append("rect")
    .attr("x", (leaf) => leaf.x0 + 4)
    .attr("y", (leaf) => leaf.y0 + 4)
    .attr("width", (leaf) => Math.max(0, leaf.x1 - leaf.x0 - 8))
    .attr("height", (leaf) => Math.max(0, leaf.y1 - leaf.y0 - 8));

  leaves
    .append("rect")
    .attr("x", (leaf) => leaf.x0)
    .attr("y", (leaf) => leaf.y0)
    .attr("width", (leaf) => Math.max(0, leaf.x1 - leaf.x0))
    .attr("height", (leaf) => Math.max(0, leaf.y1 - leaf.y0))
    .attr("fill", (leaf) => VENUE_DOMAIN_COLORS.get(leaf.data.domain) || FALLBACK_COLOR);

  leaves
    .filter((leaf) => leaf.x1 - leaf.x0 >= 54 && leaf.y1 - leaf.y0 >= 30)
    .append("text")
    .attr("class", "treemap-venue-label")
    .attr("clip-path", (leaf) => `url(#${leaf.clipId})`)
    .attr("x", (leaf) => leaf.x0 + 9)
    .attr("y", (leaf) => leaf.y0 + 19)
    .text((leaf) => leaf.data.name);

  leaves
    .filter((leaf) => leaf.x1 - leaf.x0 >= 68 && leaf.y1 - leaf.y0 >= 51)
    .append("text")
    .attr("class", "treemap-venue-count")
    .attr("clip-path", (leaf) => `url(#${leaf.clipId})`)
    .attr("x", (leaf) => leaf.x0 + 9)
    .attr("y", (leaf) => leaf.y0 + 38)
    .text((leaf) => `${format(leaf.value)} papers`);
}

function drawMatrix(catalog) {
  const width = 1180;
  const height = 650;
  const margin = { top: 142, right: 70, bottom: 58, left: 224 };
  const rows = [...catalog.families.map((family) => family.name), "Application-only"];
  const columns = [
    ...catalog.applications.map((application) => application.name),
    "No application label",
  ];
  const cells = rows.flatMap((artifact) =>
    columns.map((application) => ({
      artifact,
      application,
      count: catalog.papers.filter(
        (paper) =>
          (paper.artifact_family || "Application-only") === artifact &&
          (paper.application_domain || "No application label") === application,
      ).length,
    })),
  );

  const svg = createSvg(
    "#matrix-chart",
    width,
    height,
    "Artifact and application coverage matrix",
    "A heatmap counts papers at every intersection of artifact family and application domain.",
  );
  if (!svg) return;
  const x = d3
    .scaleBand()
    .domain(columns)
    .range([margin.left, width - margin.right])
    .padding(0.08);
  const y = d3
    .scaleBand()
    .domain(rows)
    .range([margin.top, height - margin.bottom])
    .padding(0.08);
  const color = d3
    .scaleSequential()
    .domain([0, d3.max(cells, (cell) => cell.count)])
    .interpolator((value) => d3.interpolateRgb(SURFACE, TEAL)(value));

  const columnLabels = svg
    .append("g")
    .attr("class", "matrix-labels")
    .selectAll("text")
    .data(columns)
    .join("text")
    .attr("transform", (column) => `translate(${x(column) + x.bandwidth() / 2},${margin.top - 18}) rotate(-34)`)
    .attr("text-anchor", "start")
    .text((column) => column);

  columnLabels.attr("dy", "0.32em");
  svg
    .append("g")
    .attr("class", "matrix-labels")
    .selectAll("text")
    .data(rows)
    .join("text")
    .attr("x", margin.left - 18)
    .attr("y", (row) => y(row) + y.bandwidth() / 2 + 5)
    .attr("text-anchor", "end")
    .text((row) => row);

  const cell = svg
    .append("g")
    .selectAll("g")
    .data(cells)
    .join("g")
    .on("pointerenter", (event, item) =>
      showTooltip(
        event,
        `${item.artifact} × ${item.application}`,
        `${format(item.count)} papers`,
      ),
    )
    .on("pointermove", moveTooltip)
    .on("pointerleave", hideTooltip);

  cell
    .append("rect")
    .attr("x", (item) => x(item.application))
    .attr("y", (item) => y(item.artifact))
    .attr("width", x.bandwidth())
    .attr("height", y.bandwidth())
    .attr("fill", (item) => color(item.count));
  cell
    .append("text")
    .attr("class", "matrix-value")
    .attr("x", (item) => x(item.application) + x.bandwidth() / 2)
    .attr("y", (item) => y(item.artifact) + y.bandwidth() / 2 + 5)
    .attr("text-anchor", "middle")
    .attr("fill", (item) => (item.count > 14 ? PAPER : INK))
    .text((item) => item.count);
}

function showChartError(error) {
  console.error(error);
  document.querySelectorAll(".d3-chart").forEach((chart) => {
    const message = document.createElement("p");
    message.className = "chart-error";
    message.textContent = "The interactive chart could not be loaded.";
    chart.replaceChildren(message);
  });
}

async function initializeCharts() {
  const response = await fetch("data/catalog.json");
  if (!response.ok) throw new Error(`Catalog request failed: ${response.status}`);
  const catalog = await response.json();
  drawHeroFamilies(catalog);
  drawComposition(catalog);
  drawVenues(catalog);
  drawTrend(catalog);
  drawMatrix(catalog);
}

initializeCharts().catch(showChartError);
