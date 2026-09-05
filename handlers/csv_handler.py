import csv


def read_csv(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        header = next(reader)
        rows = list(reader)

        return header, rows


def read_csv_dict(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        return list(reader)


def write_csv_dict(filename, data):
    fieldnames = ["Name", "Age", "Branch"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(data)