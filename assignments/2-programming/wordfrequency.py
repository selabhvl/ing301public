from pathlib import Path


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

    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open
    return NotImplemented
    """

    "Tok meg litt tid å feilsøke dette, men måtte bestemme enkoding for å få lest filen i hele tatt"
    "Problemet oppsto kun med voluspaa.txt, ikke small.txt"
    import codecs
    listfile = codecs.open(file_name, encoding='utf-8').readlines()
    return listfile


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

    # Tips: se på "split()"-funksjonen https://docs.python.org/3/library/stdtypes.html#str.split
    # i tillegg kan "strip()": https://docs.python.org/3/library/stdtypes.html#str.strip
    # og "lower()": https://docs.python.org/3/library/stdtypes.html#str.lower være nyttig
    return NotImplemented
    """

    "Legger alle linjene sammen til ett objekt, og så splitter alle ordene opp."
    newlines = ''.join(lines).split()
    newlines = [item.lower() for item in newlines]
    newlines = [item.strip() for item in newlines]
    "Antar det er bedre måter å gjøre dette på, men med bare 4 tegn fjernet, funker det."
    newlines = [item.strip('!') for item in newlines]
    newlines = [item.strip(',') for item in newlines]
    newlines = [item.strip('.') for item in newlines]
    newlines = [item.strip(':') for item in newlines]
    return newlines


def compute_frequency(words):
    """
    Denne funksjonen tar inn en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell
    teller hvor ofte hvert ord dykket opp i den opprinnelige innputt listen. Frekvenstabllen
    blir realisert gjennom Python dictionaires: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    F. eks. Inn ["hun", "hen", "han", "hen"], Ut: {"hen": 2, "hun": 1, "han": 1}

    return NotImplemented
    """

    "Bruker counter til å telle alle ordene, dette gir oss ein tabell av alle ordene med frekenvstall."
    count = {}
    from collections import Counter
    count = Counter(words)
    return count


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    """
    Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
    analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
    Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
    Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
    som finnes i FILL_WORDS.

    return NotImplemented
    """
    newfreq = frequency_table
    for x in FILL_WORDS:
        if x in frequency_table:
            del frequency_table[x]


    "Siden det er her listen blir sist endret, bruker jeg den for å teste."
    "Counter-objectet konverteres til ei liste av tupler, som så kan passeres inn i largest_pair"
    "Den vil da si hvilken som er størst eller om de er like."
    listfreq = list(newfreq.items())
    largest_pair(listfreq[0], listfreq[1])

    return newfreq


def largest_pair(par_1, par_2):
    """
    Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
    første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
    Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
    tallet er størst.

    # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    # kanskje du vil skrive noen flere test metoder ?!
    """
    #return NotImplemented

    if par_1 > par_2:
        print("par_1 is bigger!")
    elif par_1 == par_2:
        print("They are equal!")
    elif par_1 < par_2:
        print("par_2 is bigger!")


def find_most_frequent(frequency_table):
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.

    # Tips: se på "dict.items()" funksjonen (https://docs.python.org/3/library/stdtypes.html#dict.items)
    # og kanskje du kan gjenbruke den "largest_pair" metoden som du nettopp har laget
    """
    #return NotImplemented

    "Bruker most_common funksjonen til Counter"
    most_frequent = frequency_table.most_common(1)[0][0]
    return  most_frequent


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
