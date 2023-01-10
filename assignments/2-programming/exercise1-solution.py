from pathlib import Path


######################################
# start of functions to be implemented
######################################


# find list of word contained in the next ignoring
def lines_to_words(text: list[str]) -> list[str]:
    words = list()

    for line in text:

        # split into tokens lines at whitespaces
        # https://www.w3schools.com/python/ref_string_split.asp
        tokens = line.split()

        # filter on tokens
        for token in tokens:
            # https://www.w3schools.com/python/ref_string_split.asp
            word = token.strip(";,.:?!").lower()

            # https://www.w3schools.com/python/ref_string_isdigit.asp
            if word != '' and (not (word.isdigit())):
                words.append(word)

    return words


# find the word with the highest number of occurrences
def find_most_frequent(table):
    highest = (' ', 0)

    for pair in table.items():
        highest = largest_pair(highest, pair)

    return highest[0]


# find largest of two pairs (two-tuples) based on second item
def largest_pair(par_1: tuple[(str, int)], par_2: tuple[(str, int)]) -> tuple[(str, int)]:
    # https://www.w3schools.com/python/python_tuples.asp
    if par_1[1] > par_2[1]:
        return par_1
    else:
        return par_2


# compute a frequency table represented as a dictionary
def compute_frequency(words: list[str]):
    # https://www.w3schools.com/python/python_dictionaries.asp
    table = dict()

    for word in words:

        f = table.get(word)

        if f is None:
            table[word] = 1
        else:
            table[word] = f + 1

    return table


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


# remove items from the frequency table (dictinary) that occurs in the FILL_WORDS list
def remove_filler_words(table):
    for word in FILL_WORDS:
        if word in table:
            table.pop(word)

    return table


# https://www.w3schools.com/python/python_file_handling.asp
# optional - add exception handling when opening file: https://www.w3schools.com/python/python_try_except.asp
def read_file(filename: str) -> list[str]:
    f = open(filename, 'r')

    lines = list()

    for line in f:
        lines.append(line)

    f.close()

    return lines


####################################
# end of functions to be implemented
####################################


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
