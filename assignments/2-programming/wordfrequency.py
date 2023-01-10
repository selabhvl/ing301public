from pathlib import Path

def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def lines_to_words(lines):
    result = []
    for line in lines:
        intermediate = [ word.strip(".:;,?!").lower() for word in line.split() ]
        if not "" in intermediate:
            result += intermediate
    return result

def compute_frequency(words):
    freq_table = {}
    for word in words:
        if word.lower() not in freq_table:
            freq_table[word.lower()] = 0
        freq_table[word.lower()] += 1
    return freq_table

FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']

def remove_filler_words(frequency_table):
    for key in FILL_WORDS:
        frequency_table.pop(key, None)
    return frequency_table

def largest_pair(par_1, par_2):
    if par_1[1] >= par_2[1]:
        return par_1
    return par_2

def find_most_frequent(frequency_table):
    largest = ("", 0)
    for pair in frequency_table.items():
        largest = largest_pair(largest, pair)
    return largest[0]

def main():
    file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"
    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table)
    most_frequent = find_most_frequent(table)
    print(f"The most frequent word in {file} is '{most_frequent}'")


if __name__ == '__main__':
    main()
