# Accra Flood Exposure — GeoDev Lab Africa, Cohort One

**Project owner:** Andy Asamoah Bimpong
**Programme:** GeoDev Lab Africa, Cohort One
**Repo:** geodev-accra-flooding

## The question

Which neighbourhoods in Accra sit in flood-prone, low-lying zones — and how does that exposure relate to the city's drainage network and road infrastructure?

## Why this question

Accra floods almost every rainy season — 2015 (over 150 deaths, GOIL station explosion), 2016, and 2023 (major event at Kwame Nkrumah Circle). It's caused by low-lying terrain along the Odaw River basin combined with inadequate drainage, blocked gutters, and construction in waterways. It's well-documented, recurring, and has real accessible data — which makes it sustainable for a twelve-month project rather than a one-off report.

## Datasets

| Dataset | What it gives you | Source |
|---|---|---|
| OSM road & waterway network for Ghana | Roads, drainage channels, the Odaw River, buildings — the vector base layer | https://download.geofabrik.de/africa/ghana.html (download `ghana-latest-free.shp.zip` or `.gpkg.zip`, clip to Accra in Weeks 2–3) |
| Digital Elevation Model (SRTM, 30m) | Terrain elevation — needed to find low-lying, flood-prone areas | Google Earth Engine (`USGS/SRTMGL1_003`), or https://earthexplorer.usgs.gov |
| Satellite-detected flood extent, Oct 2023 (UNOSAT/HDX) | An actual observed flood footprint over Greater Accra & Volta Region, from Sentinel-1 imagery — ground truth to check theory against reality | https://data.humdata.org/dataset/542ca4e7-8156-4eda-b85b-ea6d403a8312 (shapefile: `FL20231018GHA_SHP.zip`) |

## What you'll have by end of week

- [X] GitHub repo created, initialized, first commit pushed
- [X] Project brief committed as README.md, with the three dataset links above
- [ ] Datasets downloaded locally (not committed — `data/README.md` explains what's excluded and why)
