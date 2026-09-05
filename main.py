import csv

# Read text file
with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()

line_count = len(content.splitlines())
word_count = len(content.split())

print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Content:", content)

# Write text file
with open("results.txt", "w", encoding="utf-8") as file:
    file.write(f"Number of lines: {line_count}\n")
    file.write(f"Number of words: {word_count}\n")

# Read CSV using csv.reader
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print("Data:", row)


# Read CSV using csv.DictReader
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            "Name:", row["Name"],
            "Age:", row["Age"],
            "Branch:", row["Branch"]
        )


# Write CSV using csv.DictWriter
with open("students_dict.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Name", "Age", "Branch"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

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