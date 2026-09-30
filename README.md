# Accra Flood Exposure

**GeoDev Lab Africa, Cohort One — Month 1**

A twelve-month project tracking flood exposure in the Accra–Volta flood extent area, built up layer by layer from spatial data to a working system.

## The question

Which roads in the Accra–Volta flood extent area were exposed to the October 2023 flood event, and how does that relate to the city's road infrastructure?

## Answer so far

**110 road segments, totalling 13.95 km, intersect the observed flood extent from the October 2023 event.**

This is a real result from an intersection between the OSM road network and the UNOSAT/HDX satellite-observed flood footprint, checked four ways (row count, map inspection, manual verification, empty-geometry check). Full detail in [`month-1-summary.md`](month-1-summary.md).

## Project documentation, week by week

| Week | What it covers | File |
|---|---|---|
| Week 1 | Project brief, question, and dataset sources | [`docs/brief.md`](docs/brief.md) |
| Week 2 | Data notes — what was downloaded, feature counts, columns, gaps | [`docs/data-note.md`](docs/data-note.md) |
| Week 3 | Reprojection, clipping, and the five data quality checks | [`docs/quality-note.md`](docs/quality-note.md) |
| Week 4 | Analysis, map, and results | [`month-1-summary.md`](month-1-summary.md) + [`maps/Road_Flood_Intersect_Map.png`](maps/Road_Flood_Intersect_Map.png) |

## Data

Raw datasets are not committed to this repository due to file size. See [`data/README.md`](data/README.md) and the source links in `docs/brief.md` for where to get them.

## Analysis-ready output

All reprojected, clipped, quality-checked layers live in `data/processed/accra_analysis_ready.gpkg` (local only, not committed — see `docs/quality-note.md` for details).
