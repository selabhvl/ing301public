from pathlib import Path

# Dette er Starterkoden til den første øvelsen i ING 301
#
# Du skal utvikle et programm som finner det hyppigste ordet i en gitt tekstfil.
# Dette høres kanskje litt komplisiert ut, men fortvil ikke!
# Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
# noen enkelte funskjoner som trengs for det hele til å virke.
# Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.


def read_file(file_name):     
    return open(file_name,"r").readlines()   

def lines_to_words(lines):
    line = str(lines)    
    for x in ["\n",",",".",":",";","?","!","\\n","'","[","]"]:           
        fixed_line = line.replace(x,"")
        line = fixed_line
    line_to_return = line.lower().split()
    return line_to_return

def compute_frequency(words):
    list = words
    myDictionary = {}
    for x in list: 
        if x in myDictionary:        
            myDictionary[x] += 1
        else:
            myDictionary[x] = 1 
    dictionary_to_return = myDictionary
    return dictionary_to_return 

FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']
def remove_filler_words(frequency_table):
    dictionary_to_return = {}
    for item in FILL_WORDS:
        if item in frequency_table:
            frequency_table.pop(item)
    dictionary_to_return = frequency_table.copy()
    return dictionary_to_return


def largest_pair(par_1, par_2):
    if par_1[1] > par_2[1]:
        largest_par_to_return = par_1
    elif par_1[1] == par_2[1]:
        largest_par_to_return = par_2  
    else: 
        largest_par_to_return = par_2
    return largest_par_to_return


def find_most_frequent(frequency_table): 
    list_of_values = list(frequency_table.values())
    list_of_keys = list(frequency_table.keys())
    value_to_return = list_of_keys[list_of_values.index(max(list_of_values))]
    return value_to_return
#                  Kan også løyses med : 
#
#   return max(frequency_table, key=frequency_table.get)
#  
# 


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
