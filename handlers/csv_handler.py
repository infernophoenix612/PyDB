import csv


def read_csv(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        header = next(reader)
        print("Header:", header)

        for row in reader:
            print("Data:", row)


def read_csv_dict(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(
                "Name:", row["Name"],
                "Age:", row["Age"],
                "Branch:", row["Branch"]
            )


def write_csv_dict(filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["Name", "Age", "Branch"]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerow({
            "Name": "Neelansh",
            "Age": 22,
            "Branch": "Mechanical"
        })

        writer.writerow({
            "Name": "Rahul",
            "Age": 21,
            "Branch": "CSE"
        })