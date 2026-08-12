#!/usr/bin/env python3
"""Compute catalog insights and render deterministic README-native SVG charts."""

from __future__ import annotations

import html
import math
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "visualization"
ARTIFACT_COMPOSITION_PATH = OUTPUT_DIR / "artifact-taxonomy-composition.svg"
FAMILY_TREND_PATH = OUTPUT_DIR / "family-trends.svg"
AXIS_MATRIX_PATH = OUTPUT_DIR / "artifact-application-matrix.svg"

APPLICATION_ONLY = "Application-only"
UNCLASSIFIED_APPLICATION = "No application label"

FAMILY_COLORS = (
    "#4C9D96",  # editorial teal
    "#66ADD0",  # clear sky blue
    "#718DCA",  # cornflower blue
    "#9380C1",  # lavender purple
    "#B777A7",  # orchid mauve
    "#D89368",  # warm apricot
)

FAMILY_TEXT_COLORS = (
    "#172033",
    "#172033",
    "#172033",
    "#172033",
    "#172033",
    "#172033",
)


@dataclass(frozen=True)
class YearFamilyBreakdown:
    year: int
    counts: tuple[int, ...]

    @property
    def total(self) -> int:
        return sum(self.counts)


@dataclass(frozen=True)
class CatalogAnalysis:
    total: int
    earliest_year: int
    latest_year: int
    family_names: tuple[str, ...]
    application_names: tuple[str, ...]
    by_year: tuple[YearFamilyBreakdown, ...]
    family_counts: tuple[int, ...]
    family_type_names: tuple[tuple[str, ...], ...]
    family_type_counts: tuple[tuple[int, ...], ...]
    application_counts: tuple[int, ...]
    matrix_row_names: tuple[str, ...]
    matrix_column_names: tuple[str, ...]
    matrix: tuple[tuple[int, ...], ...]
    artifact_classified: int
    application_classified: int
    dual_classified: int
    artifact_only: int
    application_only: int
    named_systems: int
    system_count: int
    source_count: int
    top_pairs: tuple[tuple[str, str, int], ...]


def compute_analysis(
    papers: list[dict[str, str]],
    taxonomy: dict[str, list[dict[str, object]]],
) -> CatalogAnalysis:
    family_names = tuple(
        family["name"] for family in taxonomy["artifact_families"]
    )
    application_names = tuple(
        domain["name"] for domain in taxonomy["application_domains"]
    )
    if len(family_names) != len(FAMILY_COLORS):
        raise ValueError(
            "the family chart palette must define one color per artifact family"
        )

    years = sorted({int(paper["year"]) for paper in papers})
    by_year = tuple(
        YearFamilyBreakdown(
            year=year,
            counts=tuple(
                sum(
                    paper["artifact_family"] == family
                    and int(paper["year"]) == year
                    for paper in papers
                )
                for family in family_names
            ),
        )
        for year in years
    )

    family_counter = Counter(paper["artifact_family"] for paper in papers)
    application_counter = Counter(paper["application_domain"] for paper in papers)
    family_counts = tuple(family_counter[name] for name in family_names)
    family_type_names = tuple(
        tuple(
            [artifact_type["name"] for artifact_type in family["types"]]
            + (
                ["Family-level"]
                if any(
                    paper["artifact_family"] == family["name"]
                    and not paper["artifact_type"]
                    for paper in papers
                )
                else []
            )
        )
        for family in taxonomy["artifact_families"]
    )
    family_type_counts = tuple(
        tuple(
            sum(
                paper["artifact_family"] == family_name
                and (
                    paper["artifact_type"]
                    or ("Family-level" if type_name == "Family-level" else "")
                )
                == type_name
                for paper in papers
            )
            for type_name in type_names
        )
        for family_name, type_names in zip(family_names, family_type_names)
    )
    application_counts = tuple(
        application_counter[name] for name in application_names
    )

    matrix_row_names = (*family_names, APPLICATION_ONLY)
    matrix_column_names = (*application_names, UNCLASSIFIED_APPLICATION)
    matrix = tuple(
        tuple(
            sum(
                (paper["artifact_family"] or APPLICATION_ONLY) == row_name
                and (
                    paper["application_domain"] or UNCLASSIFIED_APPLICATION
                )
                == column_name
                for paper in papers
            )
            for column_name in matrix_column_names
        )
        for row_name in matrix_row_names
    )

    artifact_classified = sum(bool(paper["artifact_family"]) for paper in papers)
    application_classified = sum(
        bool(paper["application_domain"]) for paper in papers
    )
    dual_classified = sum(
        bool(paper["artifact_family"]) and bool(paper["application_domain"])
        for paper in papers
    )
    artifact_only = sum(
        bool(paper["artifact_family"]) and not paper["application_domain"]
        for paper in papers
    )
    application_only = sum(
        not paper["artifact_family"] and bool(paper["application_domain"])
        for paper in papers
    )
    systems = [paper for paper in papers if paper["entry_kind"] == "system"]
    named_systems = sum(
        paper["name"].strip().casefold() not in {"", "n/a", "na", "none"}
        for paper in systems
    )

    top_pairs = sorted(
        (
            (family_name, application_name, matrix[row_index][column_index])
            for row_index, family_name in enumerate(family_names)
            for column_index, application_name in enumerate(application_names)
            if matrix[row_index][column_index]
        ),
        key=lambda item: (-item[2], item[0].casefold(), item[1].casefold()),
    )

    if sum(item.total for item in by_year) != artifact_classified:
        raise ValueError("yearly family counts do not match artifact coverage")
    if tuple(sum(counts) for counts in family_type_counts) != family_counts:
        raise ValueError("artifact-type counts do not match family coverage")
    if sum(sum(row) for row in matrix) != len(papers):
        raise ValueError("artifact-application matrix does not cover every paper")
    if artifact_classified + application_only != len(papers):
        raise ValueError("artifact and application-only counts do not reconcile")

    return CatalogAnalysis(
        total=len(papers),
        earliest_year=min(years),
        latest_year=max(years),
        family_names=family_names,
        application_names=application_names,
        by_year=by_year,
        family_counts=family_counts,
        family_type_names=family_type_names,
        family_type_counts=family_type_counts,
        application_counts=application_counts,
        matrix_row_names=matrix_row_names,
        matrix_column_names=matrix_column_names,
        matrix=matrix,
        artifact_classified=artifact_classified,
        application_classified=application_classified,
        dual_classified=dual_classified,
        artifact_only=artifact_only,
        application_only=application_only,
        named_systems=named_systems,
        system_count=len(systems),
        source_count=len({paper["venue_id"] for paper in papers}),
        top_pairs=tuple(top_pairs),
    )


def _escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def _axis_maximum(maximum: int) -> int:
    if maximum <= 20:
        step = 5
    elif maximum <= 50:
        step = 10
    else:
        step = 20
    return max(step, ((maximum + step - 1) // step) * step)


def _svg_header(
    width: int, height: int, title: str, description: str
) -> list[str]:
    family_variables = " ".join(
        f"--family-{index}: {color};"
        for index, color in enumerate(FAMILY_COLORS)
    )
    family_text_variables = " ".join(
        f"--family-text-{index}: {color};"
        for index, color in enumerate(FAMILY_TEXT_COLORS)
    )
    return [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {width} {height}" role="img" '
            'aria-labelledby="chart-title chart-description">'
        ),
        f'  <title id="chart-title">{_escape(title)}</title>',
        f'  <desc id="chart-description">{_escape(description)}</desc>',
        "  <style>",
        (
            "    :root { color-scheme: light; --background: #FFFFFF; "
            "--surface: #F7F9FC; --foreground: #1F2A3D; --muted: #667085; "
            "--grid: #E2E8F0; --frame: #D5DDEA; --heat: #718DCA; "
            + family_variables
            + family_text_variables
            + " }"
        ),
        (
            "    text { fill: var(--foreground); font-family: -apple-system, "
            "BlinkMacSystemFont, 'Segoe UI', sans-serif; }"
        ),
        (
            "    .title { font-family: Georgia, 'Times New Roman', serif; "
            "font-size: 28px; font-weight: 700; }"
        ),
        "    .subtitle, .note, .axis, .legend { fill: var(--muted); }",
        "    .subtitle { font-size: 15px; }",
        "    .note, .axis, .legend { font-size: 13px; }",
        "    .label { font-size: 14px; font-weight: 600; }",
        "    .value { font-size: 13px; font-weight: 700; }",
        "    .center-total { font-size: 34px; font-weight: 700; }",
        "    .center-label { fill: var(--muted); font-size: 13px; }",
        (
            "    .ring-count { font-size: 13px; font-weight: 700; "
            "pointer-events: none; }"
        ),
        (
            "    .segment-value { font-size: 12px; font-weight: 700; "
            "paint-order: stroke; stroke: var(--background); stroke-width: 3px; "
            "stroke-linejoin: round; }"
        ),
        "    .bar-segment-value { font-size: 12px; font-weight: 700; letter-spacing: 0.01em; }",
        "    .grid { stroke: var(--grid); stroke-width: 1; }",
        "    .frame { fill: none; stroke: var(--frame); stroke-width: 1; }",
        "  </style>",
        f'  <rect width="{width}" height="{height}" rx="18" fill="var(--background)"/>',
    ]


def _polar_point(
    center_x: float, center_y: float, radius: float, angle: float
) -> tuple[float, float]:
    return (
        center_x + radius * math.cos(angle),
        center_y + radius * math.sin(angle),
    )


def _donut_path(
    center_x: float,
    center_y: float,
    inner_radius: float,
    outer_radius: float,
    start_angle: float,
    end_angle: float,
) -> str:
    outer_start = _polar_point(center_x, center_y, outer_radius, start_angle)
    outer_end = _polar_point(center_x, center_y, outer_radius, end_angle)
    inner_end = _polar_point(center_x, center_y, inner_radius, end_angle)
    inner_start = _polar_point(center_x, center_y, inner_radius, start_angle)
    large_arc = int(end_angle - start_angle > math.pi)
    return (
        f"M {outer_start[0]:.2f} {outer_start[1]:.2f} "
        f"A {outer_radius} {outer_radius} 0 {large_arc} 1 "
        f"{outer_end[0]:.2f} {outer_end[1]:.2f} "
        f"L {inner_end[0]:.2f} {inner_end[1]:.2f} "
        f"A {inner_radius} {inner_radius} 0 {large_arc} 0 "
        f"{inner_start[0]:.2f} {inner_start[1]:.2f} Z"
    )


def render_artifact_composition_chart(stats: CatalogAnalysis) -> str:
    width, height = 1320, 720
    center_x, center_y = 330.0, 390.0
    inner_radius, family_radius = 95.0, 155.0
    type_inner_radius, type_outer_radius = 162.0, 245.0
    family_pad = math.radians(1.0)
    type_pad = math.radians(0.45)

    lines = _svg_header(
        width,
        height,
        "Artifact taxonomy composition",
        (
            "A two-level donut chart shows artifact families in the inner ring "
            "and artifact types in the outer ring."
        ),
    )
    lines.extend(
        [
            '  <text class="title" x="54" y="46">Artifact taxonomy composition</text>',
            (
                '  <text class="subtitle" x="54" y="73">Inner ring: '
                'artifact family · Outer ring: artifact type</text>'
            ),
            f'  <circle cx="{center_x}" cy="{center_y}" r="{type_outer_radius}" fill="var(--surface)"/>',
        ]
    )

    ring_groups = [
        (
            family_name,
            family_count,
            stats.family_type_names[index],
            stats.family_type_counts[index],
            index,
        )
        for index, (family_name, family_count) in enumerate(
            zip(stats.family_names, stats.family_counts)
        )
    ]
    ring_groups.append(
        (
            APPLICATION_ONLY,
            stats.application_only,
            (APPLICATION_ONLY,),
            (stats.application_only,),
            None,
        )
    )

    current_angle = -math.pi / 2
    for family_name, family_count, type_names, type_counts, family_index in ring_groups:
        family_span = 2 * math.pi * family_count / stats.total
        family_end = current_angle + family_span
        inner_start = current_angle + family_pad / 2
        inner_end = family_end - family_pad / 2
        family_fill = (
            f"var(--family-{family_index})"
            if family_index is not None
            else "var(--muted)"
        )
        family_text = (
            f"var(--family-text-{family_index})"
            if family_index is not None
            else "var(--background)"
        )
        lines.extend(
            [
                (
                    f'  <path d="{_donut_path(center_x, center_y, inner_radius, family_radius, inner_start, inner_end)}" '
                    f'fill="{family_fill}" stroke="var(--background)" stroke-width="2">'
                ),
                (
                    f"    <title>{_escape(family_name)}: {family_count} papers "
                    f"({family_count / stats.total:.1%})</title>"
                ),
                "  </path>",
            ]
        )
        label_angle = (current_angle + family_end) / 2
        label_x, label_y = _polar_point(
            center_x, center_y, (inner_radius + family_radius) / 2, label_angle
        )
        lines.append(
            f'  <text class="ring-count" x="{label_x:.1f}" y="{label_y + 4:.1f}" text-anchor="middle" style="fill:{family_text}">{family_count}</text>'
        )

        type_angle = current_angle
        visible_type_count = sum(bool(count) for count in type_counts)
        visible_index = 0
        for type_name, type_count in zip(type_names, type_counts):
            if not type_count:
                continue
            type_span = family_span * type_count / family_count
            type_end = type_angle + type_span
            opacity = (
                0.78
                if family_index is None
                else 0.46
                + 0.38 * visible_index / max(1, visible_type_count - 1)
            )
            lines.extend(
                [
                    (
                        f'  <path d="{_donut_path(center_x, center_y, type_inner_radius, type_outer_radius, type_angle + type_pad / 2, type_end - type_pad / 2)}" '
                        f'fill="{family_fill}" fill-opacity="{opacity:.2f}" stroke="var(--background)" stroke-width="2">'
                    ),
                    (
                        f"    <title>{_escape(family_name)} · {_escape(type_name)}: "
                        f"{type_count} papers ({type_count / stats.total:.1%})</title>"
                    ),
                    "  </path>",
                ]
            )
            type_angle = type_end
            visible_index += 1
        current_angle = family_end

    lines.extend(
        [
            f'  <circle cx="{center_x}" cy="{center_y}" r="{inner_radius - 4}" fill="var(--background)"/>',
            f'  <text class="center-total" x="{center_x}" y="{center_y - 4}" text-anchor="middle">{stats.total}</text>',
            f'  <text class="center-label" x="{center_x}" y="{center_y + 22}" text-anchor="middle">catalog papers</text>',
        ]
    )

    for family_index, (family_name, family_count) in enumerate(
        zip(stats.family_names, stats.family_counts)
    ):
        column = family_index // 3
        row = family_index % 3
        x = 650 + column * 330
        y = 154 + row * 166
        lines.extend(
            [
                f'  <rect x="{x}" y="{y - 13}" width="15" height="15" rx="3" fill="var(--family-{family_index})"/>',
                (
                    f'  <text class="label" x="{x + 24}" y="{y}">'
                    f"{_escape(family_name)} · {family_count} "
                    f"({family_count / stats.total:.1%})</text>"
                ),
            ]
        )
        visible_types = [
            (type_name, type_count)
            for type_name, type_count in zip(
                stats.family_type_names[family_index],
                stats.family_type_counts[family_index],
            )
            if type_count
        ]
        for type_index, (type_name, type_count) in enumerate(visible_types):
            opacity = 0.46 + 0.38 * type_index / max(1, len(visible_types) - 1)
            type_y = y + 28 + type_index * 21
            lines.extend(
                [
                    f'  <circle cx="{x + 7}" cy="{type_y - 4}" r="4" fill="var(--family-{family_index})" fill-opacity="{opacity:.2f}"/>',
                    (
                        f'  <text class="legend" x="{x + 20}" y="{type_y}">'
                        f"{_escape(type_name)} · {type_count} "
                        f"({type_count / stats.total:.1%})</text>"
                    ),
                ]
            )

    lines.extend(
        [
            '  <rect x="650" y="641" width="15" height="15" rx="3" fill="var(--muted)"/>',
            (
                '  <text class="label" x="674" y="654">Application-only · '
                f"{stats.application_only} "
                f"({stats.application_only / stats.total:.1%})</text>"
            ),
            (
                f'  <text class="note" x="54" y="694">All {stats.total} '
                "papers are represented; family-level records retain no finer "
                "artifact-type assignment.</text>"
            ),
            "</svg>",
        ]
    )
    return "\n".join(lines) + "\n"


def render_family_trends_chart(stats: CatalogAnalysis) -> str:
    width, height = 1200, 590
    plot_left, plot_right = 110, 1140
    count_top, count_bottom = 188, 492
    plot_width = plot_right - plot_left
    count_height = count_bottom - count_top
    slot = plot_width / len(stats.by_year)
    bar_width = min(172.0, slot * 0.54)
    maximum = _axis_maximum(max(item.total for item in stats.by_year))
    tick_step = 20 if maximum > 50 else 10

    lines = _svg_header(
        width,
        height,
        "Artifact-family paper counts over time",
        "Stacked bars compare annual paper counts across six artifact families.",
    )
    lines.extend(
        [
            '  <text class="title" x="54" y="46">Artifact-family paper counts over time</text>',
            (
                '  <text class="subtitle" x="54" y="73">Annual catalog '
                'coverage across the six artifact families</text>'
            ),
        ]
    )

    for index, family_name in enumerate(stats.family_names):
        legend_column = index % 3
        legend_row = index // 3
        x = 54 + legend_column * 370
        y = 101 + legend_row * 28
        lines.extend(
            [
                f'  <rect x="{x}" y="{y - 10}" width="13" height="13" rx="3" fill="var(--family-{index})"/>',
                f'  <text class="legend" x="{x + 21}" y="{y + 1}">{_escape(family_name)}</text>',
            ]
        )

    lines.extend(
        [
            '  <text class="label" x="54" y="171">Paper count</text>',
            f'  <rect x="{plot_left}" y="{count_top}" width="{plot_width}" height="{count_height}" rx="10" fill="var(--surface)"/>',
        ]
    )
    for tick in range(0, maximum + 1, tick_step):
        y = count_bottom - tick / maximum * count_height
        lines.extend(
            [
                f'  <line class="grid" x1="{plot_left}" y1="{y:.1f}" x2="{plot_right}" y2="{y:.1f}"/>',
                f'  <text class="axis" x="{plot_left - 13}" y="{y + 4:.1f}" text-anchor="end">{tick}</text>',
            ]
        )

    for year_index, item in enumerate(stats.by_year):
        center = plot_left + slot * (year_index + 0.5)
        x = center - bar_width / 2
        current_y = float(count_bottom)
        for family_index, count in enumerate(item.counts):
            segment_height = count / maximum * count_height
            current_y -= segment_height
            if count:
                family_name = stats.family_names[family_index]
                share = count / item.total
                lines.extend(
                    [
                        f'  <rect x="{x:.1f}" y="{current_y:.1f}" width="{bar_width:.1f}" height="{segment_height:.1f}" fill="var(--family-{family_index})" stroke="var(--background)" stroke-width="1.5">',
                        f'    <title>{_escape(item.year)} · {_escape(family_name)}: {count} papers ({share:.1%})</title>',
                        "  </rect>",
                    ]
                )
                if segment_height >= 20:
                    lines.append(
                        f'  <text class="bar-segment-value" x="{center:.1f}" y="{current_y + segment_height / 2 + 4:.1f}" text-anchor="middle" style="fill:var(--family-text-{family_index})">{count}</text>'
                    )
        lines.extend(
            [
                f'  <text class="value" x="{center:.1f}" y="{current_y - 10:.1f}" text-anchor="middle">{item.total}</text>',
                f'  <text class="label" x="{center:.1f}" y="{count_bottom + 26}" text-anchor="middle">{item.year}</text>',
            ]
        )

    lines.extend(
        [
            f'  <rect class="frame" x="{plot_left}" y="{count_top}" width="{plot_width}" height="{count_height}"/>',
            (
                f'  <text class="note" x="54" y="558">Artifact-classified '
                f'papers only (n={stats.artifact_classified}); '
                f'{stats.application_only} application-only entries are excluded. '
                f'{stats.latest_year} is incomplete.</text>'
            ),
            "</svg>",
        ]
    )
    return "\n".join(lines) + "\n"


def _balanced_lines(label: str, limit: int = 15) -> tuple[str, ...]:
    if len(label) <= limit:
        return (label,)
    words = label.split()
    best_split = min(
        range(1, len(words)),
        key=lambda index: abs(
            len(" ".join(words[:index])) - len(" ".join(words[index:]))
        ),
    )
    return (" ".join(words[:best_split]), " ".join(words[best_split:]))


def render_axis_matrix_chart(stats: CatalogAnalysis) -> str:
    width, height = 1320, 720
    matrix_left, matrix_top = 300, 170
    cell_width, cell_height = 126, 58
    matrix_width = cell_width * len(stats.matrix_column_names)
    matrix_height = cell_height * len(stats.matrix_row_names)
    maximum = max(max(row) for row in stats.matrix)
    row_totals = [sum(row) for row in stats.matrix]
    column_totals = [
        sum(row[column_index] for row in stats.matrix)
        for column_index in range(len(stats.matrix_column_names))
    ]

    lines = _svg_header(
        width,
        height,
        "Artifact–application coverage matrix",
        "A heatmap counts papers at each intersection of artifact family and application context.",
    )
    lines.extend(
        [
            '  <text class="title" x="54" y="46">Artifact–application coverage matrix</text>',
            (
                '  <text class="subtitle" x="54" y="73">Cross-axis counts; '
                'darker cells indicate denser catalog coverage</text>'
            ),
        ]
    )

    for column_index, column_name in enumerate(stats.matrix_column_names):
        center = matrix_left + cell_width * (column_index + 0.5)
        label_lines = _balanced_lines(column_name)
        start_y = matrix_top - 38 - (len(label_lines) - 1) * 8
        lines.append(
            f'  <text class="axis" x="{center:.1f}" y="{start_y}" text-anchor="middle">'
        )
        for line_index, label_line in enumerate(label_lines):
            dy = 0 if line_index == 0 else 17
            lines.append(
                f'    <tspan x="{center:.1f}" dy="{dy}">{_escape(label_line)}</tspan>'
            )
        lines.append("  </text>")

    for row_index, row_name in enumerate(stats.matrix_row_names):
        y = matrix_top + row_index * cell_height
        center_y = y + cell_height / 2
        lines.append(
            f'  <text class="label" x="{matrix_left - 18}" y="{center_y + 5:.1f}" text-anchor="end">{_escape(row_name)}</text>'
        )
        for column_index, count in enumerate(stats.matrix[row_index]):
            x = matrix_left + column_index * cell_width
            if count:
                opacity = 0.16 + 0.78 * count / maximum
                fill = "var(--heat)"
            else:
                opacity = 1.0
                fill = "var(--surface)"
            lines.extend(
                [
                    f'  <rect x="{x + 3}" y="{y + 3}" width="{cell_width - 6}" height="{cell_height - 6}" rx="8" fill="{fill}" fill-opacity="{opacity:.3f}">',
                    f'    <title>{_escape(row_name)} × {_escape(stats.matrix_column_names[column_index])}: {count} papers</title>',
                    "  </rect>",
                    f'  <text class="segment-value" x="{x + cell_width / 2:.1f}" y="{center_y + 5:.1f}" text-anchor="middle">{count}</text>',
                ]
            )
        lines.append(
            f'  <text class="value" x="{matrix_left + matrix_width + 24}" y="{center_y + 5:.1f}">{row_totals[row_index]}</text>'
        )

    lines.append(
        f'  <text class="axis" x="{matrix_left + matrix_width + 24}" y="{matrix_top - 21}" text-anchor="middle">Total</text>'
    )
    for column_index, total in enumerate(column_totals):
        center = matrix_left + cell_width * (column_index + 0.5)
        lines.append(
            f'  <text class="value" x="{center:.1f}" y="{matrix_top + matrix_height + 29}" text-anchor="middle">{total}</text>'
        )
    lines.extend(
        [
            f'  <text class="axis" x="{matrix_left - 18}" y="{matrix_top + matrix_height + 29}" text-anchor="end">Total</text>',
            f'  <rect class="frame" x="{matrix_left}" y="{matrix_top}" width="{matrix_width}" height="{matrix_height}"/>',
            (
                f'  <text class="note" x="54" y="684">All {stats.total} '
                "papers appear once. The final row and column retain entries "
                "classified on only one axis.</text>"
            ),
            "</svg>",
        ]
    )
    return "\n".join(lines) + "\n"


def build_chart_outputs(
    papers: list[dict[str, str]],
    taxonomy: dict[str, list[dict[str, object]]],
) -> dict[Path, str]:
    stats = compute_analysis(papers, taxonomy)
    return {
        ARTIFACT_COMPOSITION_PATH: render_artifact_composition_chart(stats),
        FAMILY_TREND_PATH: render_family_trends_chart(stats),
        AXIS_MATRIX_PATH: render_axis_matrix_chart(stats),
    }
