# Month 1 Summary

**GeoDev Lab Africa, Cohort One**

## The question

Which roads in the Accra–Volta flood extent area were exposed to the October 2023 flood event?

## Operation run

**Intersection: Roads × Flood Extent**

Chosen because the project already had an observed flood footprint (UNOSAT/HDX satellite data), 
not just a hypothetical hazard zone. 
Intersecting real road data against a real observed flood extent answers a direct part of the larger question — 
how exposure relates to road infrastructure — using evidence rather than estimation.

Both layers were in EPSG:32630 (UTM Zone 30N) before running the operation, 
so distance and length values came out in metres.

## Expected vs actual

- **Expected:** fewer than 30 road segments, based on visually counting roads crossing the flood polygon
- **Actual:** 110 road segments
- **Total flooded road length:** 13,955 m (≈13.95 km)

## What surprised me

The gap between the visual estimate (under 30) and the actual count (110) came down to how OSM stores roads. 
A single road that looks continuous on the map is often split into many short segments in the data — 
at junctions, bends, or other breaks. 
So one road crossing the flood zone can produce several rows in an intersection output, not one.
Counting by eye undercounts for this reason; it isn't a sign the operation went wrong.

## Checks performed

- Row count compared against expectation — explained above
- Output visually inspected on the map — sits correctly along the flood extent
- One feature manually verified — confirmed it does cross the flood polygon
- Empty geometry check (`is_empty($geometry)`) — 0 features selected, none found

## What data I still need

- Population data, to turn "roads exposed" into "people affected" (Month 2+)
- Health facility locations, to measure adaptive capacity — access to care when roads are cut
- Additional flood-extent dates, since the current single snapshot (23 Oct 2023) is likely past the flood's peak
