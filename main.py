import csv
import json

from handlers.text_handler import (
    read_text_file,
    count_lines,
    count_words,
    write_results,
)

from handlers.csv_handler import (
    read_csv,
    read_csv_dict,
    write_csv_dict,
)

from handlers.json_handler import (
    read_json,
    write_json
)

from handlers.records import Record


# =========================
# TEXT FILE
# =========================

content = read_text_file("text/input.txt")

line_count = count_lines(content)
word_count = count_words(content)

print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Content:", content)

write_results(
    "text/results.txt",
    line_count,
    word_count
)


# =========================
# CSV FILE
# =========================

header, rows = read_csv("csv/students.csv")

print("Header:", header)

for row in rows:
    print("Data:", row)

students = read_csv_dict("csv/students.csv")

for student in students:
    print(
        "Name:", student["Name"],
        "Age:", student["Age"],
        "Branch:", student["Branch"]
    )

student_data = [
    {
        "Name": "Neelansh",
        "Age": 22,
        "Branch": "Mechanical"
    },
    {
        "Name": "Rahul",
        "Age": 21,
        "Branch": "CSE"
    }
]

write_csv_dict(
    "csv/students_dict.csv",
    student_data
)

# =========================
# JSON FILE
# =========================

data = read_json("json/students.json")

print("JSON data:", data)

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

write_json(
    "json/students_output.json",
    student_data
)

# =========================
# RECORD
# =========================

student = Record("Rahul", 21, "CSE")
student.display()

data = student.to_dict()
print("Dictionary:", data)

student2 = Record("Aman", 22, "ME")
student2.display()

data = {
    "Name": "Rahul",
    "Age": "21",
    "Branch": "CSE"
}

student = Record.from_dict(data)

student.display()

try:
    invalid_student=Record("Rahul", 21, "")
    invalid_student.display()

except ValueError as error:
    print("Error:", error)