# Catalog visualizations

The SVG charts in this directory are generated from `data/papers.csv` and
`data/taxonomy.json`. They support light and dark color schemes and are embedded
in the root README's Catalog Analysis section.

Do not edit the SVGs directly. Regenerate and validate them with:

```bash
python3 scripts/generate_readme.py
python3 scripts/generate_readme.py --check
```

- `family-trends.svg` shows annual paper counts for the six artifact families.
  Application-only entries are disclosed but excluded from the family totals.
- `artifact-application-matrix.svg` counts every included paper once across the
  two independent classification axes, retaining one-axis-only entries in the
  final row or column.
