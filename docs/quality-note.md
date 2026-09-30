# Data Preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.
**Author:** Andy Asamoah Bimpong

What I reprojected, clipped, checked, and fixed.

---

## 1. Coordinate System

**Working CRS:** EPSG:32630 — WGS 84 / UTM Zone 30N

**Why:**
- Ghana falls within UTM Zone 30N
- A projected CRS (metres) is needed for accurate distance and area calculations
- Source data was in EPSG:4326 (degrees) — not suitable for that

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| Roads | EPSG:4326 | EPSG:32630 | Reprojected |
| Waterways | EPSG:4326 | EPSG:32630 | Reprojected |
| Water Extent | EPSG:4326 | EPSG:32630 | Reprojected |
| Flood Extent | EPSG:4326 | EPSG:32630 | Reprojected |
| Analysis Extent | EPSG:4326 | EPSG:32630 | Reprojected |
| DEM (SRTM) | EPSG:4326 | EPSG:32630 | Reprojected |

> Reprojecting recalculates every coordinate. Assigning a CRS only relabels the data. All layers above were reprojected.

## 2. Clipping

- **Boundary used:** Analysis Extent (HDX/UNOSAT flood dataset)
- **Features before clipping:** Roads 385,194 · Waterways 8,644 · Buildings 2,388,439 (whole-Ghana extract)
- **Scope note:** flood/water data covers only the Accra–Volta Region border area, not all of Greater Accra
- **Decision:** study area narrowed to match this footprint — see `docs/brief.md`

## 3. Five Quality Checks

| Check | Result | Action |
|---|---|---|
| CRS correct? | Confirmed EPSG:32630 on all layers | None needed |
| Nulls in key fields? | "Notes" field empty on all layers | Flagged, not fixed |
| Duplicate features? | None found (all layers, after geometry fix) | None needed |
| Geometry valid? | Waterways 276/0 invalid · Roads 9,694/0 invalid · 
Water & Flood Extent: 1 invalid each | Fixed with QGIS Fix Geometries; re-verified 0 invalid |
| Coverage spans study area? | Confirmed — no spillover or gaps | None needed |

## 4. Problems Found

**Invalid geometry — Water Extent & Flood Extent**
- Issue: one invalid geometry each (ring self-intersection)
- Cause: common in satellite-derived flood polygons from automated classification
- Fix: repaired with QGIS's Fix Geometries tool
- Verified: 0 invalid, 0 duplicates after fix
- Corrected layers replaced the originals in the final GeoPackage

**Missing "Notes" field — all layers**
- Empty across every layer
- Likely an optional metadata field left blank at source, not a processing error
- Flagged, not fixed

## 5. Analysis-Ready Output

| Property | Value |
|---|---|
| File | `data/processed/accra_analysis_ready.gpkg` |
| Format | GeoPackage |
| CRS | EPSG:32630 (WGS 84 / UTM Zone 30N) |
| Features | Roads 9,694 · Waterways 276 · Water Extent 1 · Flood Extent 1 · Analysis Extent 1 (+ 1 raster layer — DEM) |
| Produced by | QGIS — reproject, clip, Fix Geometries, export to GeoPackage |
