# fil_objekt = open("test.txt", "r+")
# # print("Naavaerende posisjon: " + str(fil_objekt.tell()))
# # fil_objekt.seek(1)
# # print("Naavaerende posisjon: " + str(fil_objekt.tell()))
# # fil_objekt.write('e')

# # innhold = fil_objekt.read()
# # print(type(innhold))
# # print(len(innhold))
# # print(innhold)
# # print(innhold[0])
# # print(innhold[1])
# #fil_objekt.write("Hello world")
# fil_objekt.close()


# JSON
import json

fil = open("test.json", mode="wt")
json.dump({
    "key": "value",
    "list": [1, 2, 3, 5]
}, fil)
fil.close()
