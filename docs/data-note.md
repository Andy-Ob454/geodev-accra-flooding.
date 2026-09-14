# Data Note — Week 2

Three datasets opened and inspected in QGIS. Details below for each.

## 1. OpenStreetMap — Ghana extract (Geofabrik)

**Source:** https://download.geofabrik.de/africa/ghana.html (`ghana-260912-free.shp.zip`)

Whole-country extract, several layers. Key ones for this project:

| Layer | Geometry | Feature count | Key columns |
|---|---|---|---|
| `gis_osm_roads_free_1` | Line (MultiLineString) | 385,194 | `osm_id`, `fclass`, `name`, `oneway`, `maxspeed`, `bridge`, `tunnel` |
| `gis_osm_waterways_free_1` | Line (MultiLineString) | 8,644 | `osm_id`, `fclass`, `width`, `name` |
| `gis_osm_buildings_a_free_1` | Polygon (MultiPolygon) | 2,388,439 | `osm_id`, `fclass`, `name`, `type` |

CRS: EPSG:4326 (WGS 84).

**Gaps/notes:** covers all of Ghana, not just Accra — needS clipping. `name` is empty for most road and waterway segments. Attribute set is minimal (5–10 columns per layer); no width/capacity data for roads, so drainage-relevant detail is limited.

## 2. UNOSAT flood mapping — Greater Accra & Volta Region (HDX)

**Source:** https://data.humdata.org/dataset/542ca4e7-8156-4eda-b85b-ea6d403a8312 (`FL20231018GHA_SHP.zip`, event date 23 Oct 2023)

| Layer | Geometry | Feature count | Key columns |
|---|---|---|---|
| Water Extent (`S1_20231023_WaterExtent_GreaterAccra_VoltaRegion`) | Polygon (MultiPolygon) | 1 | `Water_Clas`, `Confidence`, `Area_m2`, `Area_ha`, `EventCode`, `Notes` |
| Analysis Extent (`S1_20231023_AnalysisExtent_GreaterAccra_VoltaRegion`) | Polygon (MultiPolygon) | 1 | `SensorDate`, `SensorID`, `Area_m2`, `EventCode` |

CRS: EPSG:4326 (WGS 84).

**Gaps/notes:** each layer is a single dissolved multipolygon, not individual flood features — "feature count" is 1 by design, not a data-quality issue. The analysis extent covers some parts of Greater Accra **and** the Volta Region as one combined footprint, not Accra alone — meaning the project's spatial scope needs updating in the brief to reflect that the source data isn't Accra-only. Attribute fields are mostly metadata (sensor/confidence/date), not per-location detail.

## 3. SRTM Digital Elevation Model (30m)

**Source:** Google Earth Engine (`USGS/SRTMGL1_003`), exported for both Greater Accra and Volta region boundary

| Property | Value |
|---|---|
| Geometry | Raster, single band (elevation) |
| Dimensions | 6,386 × 6,809 pixels |
| Elevation range | -33 m to 510 m |
| Mean / std dev | 26.5 m / 51.1 m |
| CRS | EPSG:4326 (WGS 84) |

**Gaps/notes:** no missing/nodata pixels (100% valid coverage). The -33 m minimum is likely a known SRTM artifact near water bodies/coastline rather than a true elevation, worth flagging rather than trusting blindly.

## Scope note

The HDX flood layer's actual footprint spans Greater Accra and Volta Region together, not Accra alone as originally scoped in the project brief. `docs/brief.md` will be updated to reflect this.
