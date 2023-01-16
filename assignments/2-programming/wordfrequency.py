from pathlib import Path
# Dette er Starterkoden til den første øvelsen i ING 301
#
# Du skal utvikle et programm som finner det hyppigste ordet i en gitt tekstfil.
# Dette høres kanskje litt komplisiert ut, men fortvil ikke!
# Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
# noen enkelte funskjoner som trengs for det hele til å virke.
# Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.

def read_file(file_name):
    file = open(file_name, encoding="utf8")
    return file.readlines()

test = []
def lines_to_words(lines):
    words = []
    for line in lines:
        for word in line.split():
            if word.isalpha():
                words.append(word.lower())
            else:
                characters = filter(str.isalpha, word)
                word = ''.join(characters)
                if not (word == ''):
                    words.append(word.lower())
    return words

def compute_frequency(words):
    wordFrequencies = {}
    for word in words:
        if (word in wordFrequencies):
            wordFrequencies[word] += 1
        else:
            wordFrequencies[word] = 1
    return wordFrequencies

FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']

def remove_filler_words(frequency_table):
    for removeKey in FILL_WORDS:
        if removeKey in frequency_table:
            del frequency_table[removeKey]
    return frequency_table

def largest_pair(par_1, par_2):
    if (par_1 < par_2):
        return par_2
    else:
        return par_1
    # gjør det enkelt og returnerer par_1 hvis den er større eller lik par_2

def find_most_frequent(frequency_table):
    most_frequent = []
    max_frequency = 0
    for word in frequency_table:
        if frequency_table[word] > max_frequency:
            max_frequency = frequency_table[word]
            most_frequent = [word]
        elif frequency_table[word] == max_frequency:
            most_frequent.append(word)
    return ' '.join(most_frequent)
    # i tilfelle flere ord er like frekvente returneres alle

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
    print(table)
    print(f"The most frequent word in {file} is '{most_frequent}'")

if __name__ == '__main__':
    main()