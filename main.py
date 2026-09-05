with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()

line_count = len(content.splitlines())
word_count = len(content.split())

print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Content:", content)