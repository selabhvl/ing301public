
#%%
line = str(["words on\n", "two, lines!"])
print(line[0])
for x in ["\n",",",".",":",";","?","!","\\n","'","[","]"]:           
        fixed_line = line.replace(x,"")
        line = fixed_line
line_to_return = line.lower().split()
print(line_to_return)

#%%
# Dict test
list = ["hun", "hen", "han", "hen"]
myDictionary = {}

for x in list: 
    if x in myDictionary:           
        myDictionary[x] += 1
    else:
        myDictionary[x] = 1 
Dictionary_to_return = myDictionary
print(Dictionary_to_return)

#%%

a = ["test"] 
b = ['test']

if a == b:
    print("ok")


#%%

FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


data = {
    'det': 42,
    'odin': 10,
    'og': 9,
    'ulv': 1,
    'til': 1,
    'gud': 3,
    'som':4
    } 


print(data)

dictionary_to_return = {}
for item in FILL_WORDS:
    if item in data:
        data.pop(item)
dictionary_to_return = data.copy()        
        
print(dictionary_to_return)




#%%
par1,par2 = ('Hallo', -3), ("World", -3)


if par1[1] > par2[1]:
    largest_par = par1
    
elif par1[1] == par2[1]:
    largest_par = par2
     
else: 
    largest_par = par2
    
print(largest_par)    



# %%
data = {
    'hei': 23,
    'sjelden': 1,
    'oftest': 9000,
    'answer': 42
    }

list_of_values = list(data.values())
list_of_keys = list(data.keys())

print(list_of_keys[list_of_values.index(max(list_of_values))])

# max(data, key=data.get)


#nei
# if par_1[1] > par_2[1]:
#         largest_par_to_return = par_1
#     elif par_1[1] == par_2[1]:
#         largest_par_to_return = par_2  
#     else: 
#         largest_par_to_return = par_2
#     return largest_par_to_return
