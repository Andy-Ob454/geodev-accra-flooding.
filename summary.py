import csv


def load_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def get_numbers(rows, column):
    numbers = []
    for row in rows:
        raw = row[column].strip().replace(",", "")
        if raw != "" and raw.upper() != "NA":
            numbers.append(float(raw))
    return numbers


def summarise_column(numbers):
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
    }


def summarise_all(rows, columns):
    for column in columns:
        s = summarise_column(get_numbers(rows, column))
        print(column, "count:", s["count"], "smallest:", s["min"],
              "largest:", s["max"], "average:", round(s["mean"], 2))


rows = load_rows("flooded_roads.csv")
summarise_all(rows, ["id", "length_m"]) 