Data preparation

Week 3 deliverable. GeoDev Lab Africa, Cohort One. Author: Andy Asamoah Bimpong.

What I reprojected, what I clipped, what I checked, and what I fixed.

1. Coordinate system decisions

Working CRS: EPSG:32630 — WGS 84 / UTM Zone 30N

Why this one: Ghana falls within UTM Zone 30N. 
A projected CRS in metres is needed for accurate distance and area calculations. 
The source data was in EPSG:4326 (degrees), which doesn't support that.

Dataset	CRS as downloaded	CRS after	Operation
Roads	EPSG:4326	EPSG:32630	Reprojected
Waterways	EPSG:4326	EPSG:32630	Reprojected
Water Extent	EPSG:4326	EPSG:32630	Reprojected
Flood Extent	EPSG:4326	EPSG:32630	Reprojected
Analysis Extent	EPSG:4326	EPSG:32630	Reprojected
DEM (SRTM)	EPSG:4326	EPSG:32630	Reprojected

Reprojecting recalculates every coordinate. 
Assigning a CRS only relabels the data. 
All layers above were reprojected, not just relabelled.

2. Clipping to the study area
Boundary used: Analysis Extent (from the HDX/UNOSAT flood dataset)
Features before clipping: Roads 385,194 · Waterways 8,644 · Buildings 2,388,439 (whole-Ghana extract)

Scope note: the flood/water data covers only the Accra–Volta Region border area, not all of Greater Accra. 
The study area was narrowed to match this footprint rather than a wider boundary the data doesn't actually cover. 
See docs/brief.md.

3. The five quality checks
Check	Result	Action taken
Is the CRS what I think it is?	Confirmed EPSG:32630 on all layers	None needed
Are there nulls in the fields I need?	"Notes" field empty on all layers;
other fields complete	Flagged, not fixed — doesn't affect analysis
Are there duplicate features?	None found (Waterways, Roads, Analysis Extent);
none found on Water/Flood Extent after geometry fix	None needed
Is the geometry valid?	Waterways 276 valid/0 invalid · Roads 9,694 valid/0 invalid ·
 Water Extent and Flood Extent: 1 invalid each (ring self-intersection)
Fixed using QGIS Fix Geometries; re-verified 0 invalid
Does coverage span the whole study area?	Confirmed —
no spillover or gaps against the Analysis Extent boundary	None needed
5. Problems found, and what I did

Invalid geometry — Water Extent and Flood Extent Both layers had one invalid geometry each, 
caused by ring self-intersection — a known issue with satellite-derived flood polygons from automated classification. 
Fixed with QGIS's Fix Geometries tool, then re-checked: 0 invalid, 0 duplicates. 
The corrected layers replaced the originals in the final GeoPackage.

Missing "Notes" field — all layers Empty across every layer. 
Appears to be an optional metadata field left blank at the source, not an error introduced during processing.
Flagged, not fixed.

5. The analysis-ready output
File: data/processed/accra_analysis_ready.gpkg
Format: GeoPackage
CRS: EPSG:32630 (WGS 84 / UTM Zone 30N)
Features: []
Produced by: QGIS — reproject, clip, Fix Geometries, export to GeoPackage
