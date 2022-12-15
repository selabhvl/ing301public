# Dette Starterkoden for første øvelsen i ING 301 #

###################################################################################
# Her kommer det litt glue-kode som vi har gitt deg som rammerverk                #
# Bare ignorer dette for nå og bare konsentrere deg på det som kommer lenger nede #
###################################################################################

from pathlib import Path

def to_tokens(text):
    result = []
    text = text.strip()
    word = ''
    for c in text:
        if c.isspace() or c == ';' or c == ',' or c == '.' or c == ':' or c == '?':
            if len(word) != 0:
                result.append(word.lower())
            word = ''
        else:
            word += c
    if len(word) != 0:
        result.append(word.lower())
    return result


def findmax(index):
    max = ("Filen var tom !!!", -1)
    for pair in index.items():
        max = max_pair(max, pair)
    return max


def findmax_file(address):
    file_content = read_file(address)
    word_list = to_tokens(file_content)
    index = make_index(word_list)
    index = clear_index(index)
    max_pair = findmax(index)
    print(max_pair)
    return max_pair[0]


############################################
#                                          #
# Her begynner koden du skal viderutvikle! #
#                                          #
############################################

FYLLORD = ['og','dei','i','eg','som','det','han','til','skal','på','for','då','ikkje','var','vera']


def max_pair(par_1, par_2):
    """
      TODO: Denne funksjonen forventer å få to par (tuple) som inputt.
      Paret består av et ord og et tall, f eks. ("Hei", 42).
      Funksjonen må gi tilbake det paret som inneholde det større tallet!
    """
    return NotImplemented  # TODO: Du må fjerne denne linjen og skrive noe eget som fungerer !


def make_index(ordlist):
    """
        TODO: Denne funksjonen forventer å få en liste av ord som inputt.
        Som resultat må funksjonen gi tilbake en 'indeks'.
        Dvs. en dictionary som har 'ord' fra den gitte listen som nøkkel.
        Verdien til en nøkkel er et tall som sier hvor ofte ordet ble
        nevnt i gitte listen. 

        Tipps: Bruk max_pair metoden fra før!
    """
    result = { }
    # TODO: Din kode her! Kanskje starte med en løkke ;-)
    return result


def clear_index(index):
    """ TODO: Her må du gjøre et eller annet for å blit kvitt 
        fylleord som "og", "skal", "eller" i indeksen
    """
    return index


def read_file(adresse):
    """ TODO: Denne funksjonen får en filsystem-adresse som argument.
        Som resultat skulle den gi tilbake en string som representere
        innholdet til den filen som befinner seg bak gitt adresse.
    """
    return "" # TODO: Du må erstatte denne linjen


############################################################
#                                                          #
#### Her slutter delen av filen som er relevant for deg ####
#                                                          #
############################################################

if __name__ == '__main__':
    file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"
    print(f"The most frequent word in {file} is '{findmax_file(file)}'")
