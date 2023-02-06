
def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    liste=[]
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            liste.append(line)
        print(liste)
    file.close()
    return liste


liste1 = read_file('small.txt')


def lines_to_words(lines):
    new_list = []
    for word in lines:
        x = word.split()
        new_list.append(x)
    flattened = [val for sublist in new_list for val in sublist]
    flattened_2 = list(map(str.lower,flattened))
    flattened_fin = [i.strip('!') for i in flattened_2]


    print(flattened_fin)
    return flattened_fin

lines_to_words(liste1)


list2 = lines_to_words(liste1)

def compute_frequency(words):
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    print(counts)
    return counts

compute_frequency(list2)
x = compute_frequency(list2)


def remove_filler_words(frequency_table):
    FILLER_WORDs = ['er', 'og',]
    for element in FILLER_WORDs:
        if element in frequency_table:
            frequency_table.pop(str(element))
        else:
            pass
    print(frequency_table)
    return frequency_table

remove_filler_words(x)
o = remove_filler_words(x)

v = list(remove_filler_words((x)).items())
print(v)


def largest_pair(par_1, par_2):
    if par_1[1] > par_2[1]:
        print(str[par_1[0]] + ' er størst')
    elif par_1[1] < par_2[1]:
        print(str[par_2[0]] + ' er størst')
    elif par_1[1] == par_2[1]:
        print('Begge parene er like store')
    return

largest_pair(v[0], v[1])

def find_most_frequent(frequency_table):
    track = {}
    for key, value in frequency_table.items():
        if value not in track:
            track[value] =0
        else:
            track[value] +=1
    print(max(track, key=track.get))

find_most_frequent(o)



