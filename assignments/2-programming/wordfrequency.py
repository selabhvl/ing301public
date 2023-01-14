from pathlib import Path

# Dette er Starterkoden til den første øvelsen i ING 301
#
# Du skal utvikle et programm som finner det hyppigste ordet i en gitt tekstfil.
# Dette høres kanskje litt komplisiert ut, men fortvil ikke!
# Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
# noen enkelte funskjoner som trengs for det hele til å virke.
# Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.


def read_file(file_name: str) -> list:
    """
    Denne funksjonen får et filnavn som argument og gir tilbake
    en liste av strings som representerer linjene i filen.

    :param file_name: navnet til filen som skal leses.
    :return: en liste av linjer i filen.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines


def lines_to_words(lines: list) -> list:
    """
    Denne funksjonen tar en liste av setninger og returnerer en liste med ord
    ved hjelp av .split(), .strip() og .lower().

    :param lines: Liste av setninger (str)
    :return: Liste av ord (str)
    """
    words = []
    for line in lines:
        word = word.strip(".,:;!?").lower()
        if word:
            words.append(word)
    return words


def compute_frequency(words: list[str]) -> dict[str, int]:
    """
    Denne funksjonen tar en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell teller
    hvor ofte et ord dukker opp i den opprinnelige input-listen. Frekvenstabellen blir realisert gjennom
    Python Dictionaries.

    Eksempel: inn ["hun", "hen", "han", "hen"]
    Ut: {"hen": 2, "hun": 1, "han": 1}.

    :param words: liste av ord som skal telles.
    :return: en dictionary hvor "key" er ordet og verdien er antall ganger ordet dukker opp i input-listen.
    """
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table: dict[str, int]):
    """
    Funksjonen tar inn en frekvenstabell og fjerner koblingsord som "og", "eller", "jeg", "da".
    Koblingsordene blir deretter fjernet fra frekvenstabellen.

    :param frequency_table: En frekvenstabell man ønsker å fjerne koblingsord fra.
    :return: En frekvenstabell som har fått fjernet koblingsordene.
    """
    for word in FILL_WORDS:
        if word in frequency_table:
            del frequency_table[word]
    return frequency_table


def largest_pair(par_1, par_2):
    """
    Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
    første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
    Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
    tallet er størst.
    """
    # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    # kanskje du vil skrive noen flere test metoder ?!
    return NotImplemented  # TODO: Du må erstatte denne linjen


def find_most_frequent(frequency_table):
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    # Tips: se på "dict.items()" funksjonen (https://docs.python.org/3/library/stdtypes.html#dict.items)
    # og kanskje du kan gjenbruke den "largest_pair" metoden som du nettopp har laget
    return NotImplemented  # TODO: Du må erstatte denne linjen


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
