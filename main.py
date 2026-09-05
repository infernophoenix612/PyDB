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

read_csv("csv/students.csv")

read_csv_dict("csv/students.csv")

write_csv_dict("csv/students_dict.csv")

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