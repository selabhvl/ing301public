from pathlib import Path
# Dette er Starterkoden til den første øvelsen i ING 301
#
# Du skal utvikle et programm som finner det hyppigste ordet i en gitt tekstfil.
# Dette høres kanskje litt komplisiert ut, men fortvil ikke!
# Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
# noen enkelte funskjoner som trengs for det hele til å virke.
# Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.

def read_file(file_name):
    try:
        with open(file_name, encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []
    return lines


def lines_to_words(lines):
    words = []
    for line in lines:
        for word in line.split():
            word = word.strip(".:;,!?")
            word = word.lower()
            if word:  
                words.append(word)
    return words

def compute_frequency(words):
    frequency_table = {}
    for word in words:
        if word in frequency_table:
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1
    return frequency_table



FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    for word in FILL_WORDS:
        if word in frequency_table:
            del frequency_table[word]
    return frequency_table


def largest_pair(par_1, par_2): 
    if par_1[1] > par_2[1]:
        return par_1
    elif par_1[1] < par_2[1]:
        return par_2
    elif par_1[1] == par_2[1]:
        return "The two pairs are equal"


def find_most_frequent(frequency_table):
    most_frequent_word = None
    highest_frequency = 0
    for word, frequency in frequency_table.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            most_frequent_word = word
    return most_frequent_word
    
############################################################
#                                                          #
# Her slutter dendelen av filen som er relevant for deg ;-)#
#                                                          #
############################################################


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