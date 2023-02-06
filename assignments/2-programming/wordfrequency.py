import re
from pathlib import Path
from string import punctuation

"""
Dette er Starterkoden til den første øvelsen i ING 301
Du skal utvikle et programm som finner det mest brukte(hyppigste) ordet i en gitt tekstfil.
Dette høres kanskje litt komplisiert ut, men fortvil ikke!
Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
noen enkelte funskjoner som trengs for det hele til å virke.
Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.
"""
'''
# Fra forelesning
file = open("file/location", "r")
lines = file.readLines()
counter = 0
gps_points = []
for line in lines:
    if counter > 0:
        gps_points.append(line)
    counter += 1

first = gps_points[0]
first_split = first.split(',')
first_timestamp = first.split(0)
print(first_timestamp)
print(type(first_timestamp))
'''

"""
Denne funksjonen får et filnavn som argument og skal gi
tilbake en liste av tekststrenger som representerer linjene i filen.
"""


def read_file(file_name):
    myLines = []
    with open(file_name) as file:
        for line in file:
            myLines.append(line)



    # file = open(file_name, "r", encoding="utf-8")



    # for line in file:
         # myLines.append(line.strip()) # Through some magic this removes newlines in our list.



    #filetext = file.read()
    # print(myLines) # debugging
    return myLines

def lines_to_words(lines):
    doneList = []
    breaklineOfDeath = ['']

    for word in lines:
         r = re.compile(r'[\s\n{},.;:]+'.format(re.escape(punctuation))) # My dumb way of regexing the world.
         wordList = r.split(word) # split using regex
         doneList += wordList    #add split word to a list

    wordListLower = [element.lower() for element in doneList]

    # for word in wordListLower:
    #     if word in breaklineOfDeath:
    #         wordListLower.remove(word)
    # the same as
    finalList = [word for word in wordListLower if word not in breaklineOfDeath]

    return finalList

    """
    Denne funksjonen får en liste med strenger som input (dvs. linjene av tekstfilen som har nettopp blitt lest inn)
    og deler linjene opp i enkelte ord. Enhver linje blir delt opp der det er blanktegn (= whitespaces).

    Desto videre er vi bare interessert i faktiske ord, dvs. alle punktum (.), kolon (:), semikolon (;),
    kommaer (,), spørsmåls- (?) og utråbstegn (!) skal fjernes underveis.

    Til sist skal alle ord i den resulterende listen være skrevet i små bokstav slik at "Odin" og "odin"
    blir behandlet likt.

    OBS! Pass også på at du ikke legge til tomme ord (dvs. "" eller '' skal ikke være med) i resultatlisten!

    F. eks: Inn: ["Det er", "bare", "noen få ord"], Ut: ["Det", "er", "bare", "noen", "få", "ord"]
    """

    # Tips: se på "split()"-funksjonen https://docs.python.org/3/library/stdtypes.html#str.split
    # i tillegg kan "strip()": https://docs.python.org/3/library/stdtypes.html#str.strip
    # og "lower()": https://docs.python.org/3/library/stdtypes.html#str.lower være nyttig


def compute_frequency(words):
    """
    Denne funksjonen tar inn en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell
    teller hvor ofte hvert ord dykket opp i den opprinnelige innputt listen. Frekvenstabllen
    blir realisert gjennom Python dictionaires: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    F. eks. Inn ["hun", "hen", "han", "hen"], Ut: {"hen": 2, "hun": 1, "han": 1}
    """
    frequency = dict()
    for word in words:  # go through what we are sent
        if word in frequency:   # Word exists.
            frequency[word] += 1  # Up count by one.
        else:   # Word doesnt exist
            frequency[word] = 1  # Set count to one.

    # Deletes ASCII newline space which cant be eliminated with UTF-8 Regex. (Not necessary anymore)
    # del frequency[max(frequency, key=frequency.get)]

    return frequency


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    """
    Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
    analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
    Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
    Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
    som finnes i FILL_WORDS.
    """

    table = frequency_table #gets sent table
                                            # #cant work on a table that is being itterated on
    for word, count in list(table.items()): # goes through said table and edits it by making a copy to a new list.
        for fillWord in FILL_WORDS:         # check words we cant use
            if word == fillWord:            # illegal word detected?
                del table[word]             # NOT ON MY WATCH YEET THAT SH

    return table


def largest_pair(par_1, par_2):
    """
    Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
    første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
    Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
    tallet er størst.
    """
    # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    # kanskje du vil skrive noen flere test metoder ?!

    if par_1[1] > par_2[1]:  #Lmao unused code
        return par_1        #dont need to overthink this.
    else:
        return par_2


def find_most_frequent(frequency_table):
    return max(frequency_table, key=frequency_table.get)

    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    # Tips: se på "dict.items()" funksjonen (https://docs.python.org/3/library/stdtypes.html#dict.items)
    # og kanskje du kan gjenbruke den "largest_pair" metoden som du nettopp har laget


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
