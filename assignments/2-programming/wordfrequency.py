from pathlib import Path

"Vi skal åpne en fil som er lokalt plassert og hente innholdet og bearbeide innholdet."
"Vi begynner først med å "

def read_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as fil:
            lines = fil.readlines()
        return lines
    except:
        print("Feilkode: 1_Feil_Med_Fil_lesing")

"Vi skal nå ha åpnet filen og hentet filinholdet i 8bit tekst"

def lines_to_words(lines):
    innhold = []
    try:
        for line in lines:
            tegn = [ word.strip(".:;,?!").lower() for word in line.split() ]
            if not "" in tegn:
                innhold += tegn
        return innhold
    except:
        print("Feilmelding: 2_Feil_Under_Filtrering_Av_Tekst/Innhold") 
            
"Vi skal nå ha rene bokstaver uten tegn! /filtrert tekst om du vil"

def compute_frequency(words):
    freq_table = {}
    try:
        for word in words:
            if word.lower() not in freq_table:
                freq_table[word.lower()] = 0
            freq_table[word.lower()] += 1
        return freq_table
    except:
        print("Feilmelding: 3_Feil_Under_Kartlegging_Av_Ord")


""

FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']

""

def remove_filler_words(frequency_table):
    try:
        for key in FILL_WORDS:
            frequency_table.pop(key, None)
        return frequency_table
    except:
        print("feilmelding: 4_Programerer_Er_for_Dum_Til_AA_Gjøre_Enkle_For_Kommandoer")

""

def largest_pair(par_1, par_2):

    if par_1[1] >= par_2[1]:
        return par_1
    return par_2

"Er en if komando, bruker ikke try her, hva kan gå galt her. -famous last words"

def find_most_frequent(frequency_table):
    largest = ("", 0)
    try:
        for pair in frequency_table.items():
            largest = largest_pair(largest, pair)
        return largest[0]
    except:
        print("Feilmelding: 5&6_Nå_Kan_Du_Verken_Regne_Eller_Programmere")

""

def main():
    file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"
    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table)
    most_frequent = find_most_frequent(table)
    print(f"The most frequent word in {file} is '{most_frequent}'")

""

if __name__ == '__main__':
#if __name__ == "__main__":
    main()
