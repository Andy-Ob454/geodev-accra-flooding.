import csv

with open("flooded_roads.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

# Column 1: length_m (numbers)
lengths = []
for row in rows:
    lengths.append(float(row["length_m"]))

length_summary = {
    "count": len(lengths),
    "min": min(lengths),
    "max": max(lengths),
    "mean": sum(lengths) / len(lengths),
}
print("length_m:", length_summary)

# Column 2: fclass (text)
fclass_counts = {}
for row in rows:
    road_type = row["fclass"]
    if road_type in fclass_counts:
        fclass_counts[road_type] += 1
    else:
        fclass_counts[road_type] = 1
print("fclass:", fclass_counts)