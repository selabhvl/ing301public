from pathlib import Path

def read_file(file_name):
    file = open(file_name, 'r')                                 #Åpner filen
    filecontent = file.read()                                   #Leser filen

    file.close()                                                #Lukker filen

    return filecontent                                          #Retunerer svaret


def lines_to_words(lines):
    for ord in lines:                                           #Kjører gjennom alle ordene i listen
        ordSplittet = lines.split()                             #Bruker lines.split for å splitte alle ordene i listen

    ordStrippet = [i.strip(' ,.:;!?') for i in ordSplittet]     #Sletter alle mellomrom, komma, ., :, ;, ! og ?

    ordFerdig = [i.lower() for i in ordStrippet]                #Gjør alle bokstavene små

    return ordSplittet


def compute_frequency(words):
    wordsNumber = {}                                            #Lager en dictionary
    for item in words:                                          #Finner alle ordene i listen
        count=words.count(item)                                 #Her finner vi ut hvor mange av hver det er i listen
        wordsNumber.update({item:count})                        #Skriver de i dictionary i ønsket oppsett

    return wordsNumber


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    for RemoveWord in FILL_WORDS:                               #Finner alle enhetene i dictionaryen
        if RemoveWord in frequency_table:                       #Hvis et av ordene i FILL_WORDS er i dictionaryen motatt
            del frequency_table[RemoveWord]                     #Slettes de

    return frequency_table


def largest_pair(par_1, par_2):
    if par_1[1] > par_2[1]:
        return par_1
    elif par_1[1] < par_2[1]:
        return par_2
    else:
        return par_1                                            #retunerer par_1    


def find_most_frequent(frequency_table):
    mostUsed = ("", 0)                                          #Lager en ny tuple som kan brukes i sammenligning

    for word, used in frequency_table.items():                  #Sjekker alle ordene i tabellen
        mostUsed = largest_pair(mostUsed, (word,used))          #Sammenligner, og får tilbake den som er brukt mest i hele listen

    return mostUsed



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

