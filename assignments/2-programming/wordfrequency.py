from pathlib import Path
import random
import test_wordfrequency

# Dette er Starterkoden til den første øvelsen i ING 301
#
# Du skal utvikle et programm som finner det hyppigste ordet i en gitt tekstfil.
# Dette høres kanskje litt komplisiert ut, men fortvil ikke!
# Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
# noen enkelte funskjoner som trengs for det hele til å virke.
# Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.


def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    # Reading file contents
    file = open(file_name, mode = "r", encoding = "utf8")
    filecontent = file.read()

    # Spliting filecontent on linebreaks and saving in new list
    file_lines = filecontent.split('\n')
    file.close()

    return file_lines

    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open


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

    file_lines = lines
    words_list = []

    #rolling through the elements of the list
    for line_words in file_lines:

        #splitting the list on ' '(blankspace) into a new list 
        split_content = line_words.split(' ')
        #set of chars to be removed from the list
        char_set = {",", "?", "!", ".", ":", ";", "-", "", ''}

        #rolling throught the new list and checking for lone instances of the char_set in the list
        for content in split_content:
            #if char_set is in content dont append to words_list
            if content not in char_set:

                words_list.append(content.strip(',.:;!?\n').lower())
            
        for index, word in enumerate(words_list):
            if word == '':
                words_list.pop(index)

    return words_list


def compute_frequency(words):
    """
    Denne funksjonen tar inn en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell
    teller hvor ofte hvert ord dykket opp i den opprinnelige innputt listen. Frekvenstabllen
    blir realisert gjennom Python dictionaires: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    F. eks. Inn ["hun", "hen", "han", "hen"], Ut: {"hen": 2, "hun": 1, "han": 1}
    """

    word_freq = {}
    #looping through the list of words given and adding them to the word_freq dict with a value of 1 if they are not all ready in the dict
    #or if they are allready in the dict then upping the value(word count) by 1
    for word in words:
        if word in word_freq:
            word_freq[word] += 1

        else:
            word_freq[word] = 1

    return word_freq



FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han',
              'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    """
    Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
    analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
    Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
    Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
    som finnes i FILL_WORDS.
    """
    newdict = {}

    #unpacking given dict and writing to newdict if it is not contained in the list FILL_WORDS
    for stuffkey,stuffvalue in frequency_table.items():
        if stuffkey not in FILL_WORDS:
            newdict[stuffkey] = stuffvalue

    #print(newdict)
    return newdict


def largest_pair(par_1, par_2):
    """
    Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
    første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
    Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
    tallet er størst.
    """
    #comparing value element size choosing largest
    if par_1[1] > par_2[1]:
        bIg_pair = par_1
    elif par_1[1] < par_2[1]:
        bIg_pair = par_2

    #If pairs are equal return a list of both pairs
    elif par_1[1] == par_2[1]:
        bIg_pair = [par_1, par_2]
        
    return bIg_pair


def find_most_frequent(frequency_table):
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Denne funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    """
    source for bubble sort used: https://stackoverflow.com/questions/52551033/bubble-sorting-in-dictionary-in-python
    i decided to do it this way as i got a Type error when comparing the 2 tuples so maybe inner node somewhere i cant find the problem
    """
    #converting dict to list objet
    freq_list = list(frequency_table.items())


    list_len = len(freq_list) - 1 #-1 so it does not run 1 unneeded time

    #bubble sort algoritm for sorting the list largest to smalest value element
    for count in range(list_len, -1, -1):
        swapped = False
        for i in range(count):
            if freq_list[i][1] < freq_list[i + 1][1]:
                #swapping elements if one element i + 1 is larger
                freq_list[i], freq_list[i + 1] = freq_list[i + 1], freq_list[i]
                swapped = True

        #breaking when sorting is done
        if not swapped:
            break

    
    most_freq = freq_list[0]

    return most_freq[0]


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
