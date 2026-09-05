import csv
import json

# Read text file
with open("text/input.txt", "r", encoding="utf-8") as file:
    content = file.read()

line_count = len(content.splitlines())
word_count = len(content.split())

print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Content:", content)

# Write text file
with open("text/results.txt", "w", encoding="utf-8") as file:
    file.write(f"Number of lines: {line_count}\n")
    file.write(f"Number of words: {word_count}\n")

# Read CSV using csv.reader
with open("csv/students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print("Data:", row)


# Read CSV using csv.DictReader
with open("csv/students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            "Name:", row["Name"],
            "Age:", row["Age"],
            "Branch:", row["Branch"]
        )


# Write CSV using csv.DictWriter
with open("csv/students_dict.csv", "w", newline="", encoding="utf-8") as file:
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

# Read JSON file
with open("json/students.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("JSON data:", data)


# Write JSON file
student_data = {
    "students": [
        {
            "name": "Neelansh",
            "age": 22,
            "branch": "Mechanical"
        },
        {
            "name": "Rahul",
            "age": 21,
            "branch": "CSE"
        }
    ]
}

with open("json/students_output.json", "w", encoding="utf-8") as file:
    json.dump(student_data, file, indent=4)