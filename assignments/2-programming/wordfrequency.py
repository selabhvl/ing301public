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
        for word in line.split():
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


def largest_pair(par_1: tuple[str, int], par_2: tuple[str, int]) -> tuple[str, int]:
    """
    Funksjonen får to tupler/par som input, hvor den første komponenten er et ord (str),
    og den andre komponenten er et tall (int).
    Funksjonen sammenligner så tall-komponenten [1] i begge tuplene,
    og returnerer det paret hvor tallet er størst. Dersom begge tallene er identiske,
    returneres par_1.

    :param par_1: En Tuple som inneholder et ord og en verdi.
    :param par_2: En Tuple som inneholder et ord og en verdi.
    :return: Returnerer tuplen som har det største tallet.
    """
    if par_1[1] > par_2[1]:
        return par_1
    elif par_1[1] < par_2[1]:
        return par_2
    else:
        return par_1    # eventuelt 'return par_2' --> har ikke noe å si siden tallene er like.


def find_most_frequent(frequency_table: dict[str, int]) -> tuple[str, int]:
    """
    Funksjonen tar frekvenstabellen som input og finner ordet som har gjentas flest ganger.
    :param frequency_table: frekvenstabell for å finne ordet med høyest frekvens.
    :return: en Tuple som inneholder det ordet som gjentas flest ganger, samt hvor mange ganger det gjentas.
    """
    return max(frequency_table.items(), key=lambda x: x[1])


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
