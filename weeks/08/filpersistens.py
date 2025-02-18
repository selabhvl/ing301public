import pathlib

mappe = pathlib.Path.cwd()
print(mappe.absolute())

fil = open("test.txt",  mode="at", newline='\n')
fil.write("hvordan har du det")
# innhold = fil.read()
# print(type(innhold))
# print(innhold[0])
# print(innhold[1])
# print(innhold[2])
# print(innhold[3])
# print(innhold[4])
# print(innhold[5])
# print(innhold[6])
fil.close()