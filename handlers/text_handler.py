def read_text_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def count_lines(content):
    return len(content.splitlines())


def count_words(content):
    return len(content.split())


def write_results(filename, line_count, word_count):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Number of lines: {line_count}\n")
        file.write(f"Number of words: {word_count}\n")