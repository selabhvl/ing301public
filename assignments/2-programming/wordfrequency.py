from pathlib import Path


def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """

    # Open file:
    textfile = open(file_name, 'r') # Opens text file.

    # Add lines to list:
    lines = []
    for line in textfile:
        line = line.rstrip() # Strips line.
        lines.append(line) # Adds line to list.

    return lines


def lines_to_words(lines):
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

    # Split words in list:
    words = []
    for line in lines:
        for word in line.split():
            word = word.strip('.:;,?!- ').lower() # Strips and converts word to lowercase.
            words.append(word) # Adds word to list.

    return words


def compute_frequency(words):
    """
    Denne funksjonen tar inn en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell
    teller hvor ofte hvert ord dykket opp i den opprinnelige innputt listen. Frekvenstabllen
    blir realisert gjennom Python dictionaires: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    F. eks. Inn ["hun", "hen", "han", "hen"], Ut: {"hen": 2, "hun": 1, "han": 1}
    """

    # Compute word frequency:
    frequency_table = {}
    for word in words:
        if (word in frequency_table):
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1 # Adds word to dictionary.
    
    return frequency_table


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    """
    Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
    analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
    Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
    Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
    som finnes i FILL_WORDS.
    """

    # Make a copy of dictionary keys:
    frequency_table_copy = tuple(frequency_table.keys()) # This prevents error when iterating through the dictionary while deleting words.
    
    # Remove filler words from dictionary:
    for word in frequency_table_copy:
        if word in FILL_WORDS:
            del frequency_table[word] # Removes word from dictionary if it's a filler word.

    return frequency_table


def largest_pair(par_1, par_2):
    """
    Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
    første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
    Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
    tallet er størst.
    """
    
    # Define largest pair:
    #if (par_1[1] > par_2[1]):
    #    # Par_1 has the highest frequency.
    #    return par_1[0]
    #    return "NUMMER 1"
    #elif (par_1[1] < par_2[1]):
    #    # Par_2 has the highest frequency.
    #    return par_2[0]
    #    return "NUMMER 2"
    #else:
    #    # Par_1 and par_2 has the same frequency.
    #    return "LIK"
    return NotImplemented


def find_most_frequent(frequency_table):
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    #print(frequency_table)

    # Compute most frequent word:
    words = list(frequency_table.keys())
    frequency = list(frequency_table.values())
    most_frequent = words[frequency.index(max(frequency))]
    
    return most_frequent


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
