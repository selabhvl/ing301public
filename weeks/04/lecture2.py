a = "World"
x = 23
y = 3.1415
print("Hello " + a)
print("Goodbye " + a)
print(2 + 3)
# dette funker ikke: print(a + 3)

print(type(a))
print(type(x))
print(type(y))
print(type(True))
print(type(False))

print("Na" * 10 + " Batman!")


# Definer en funksjon
def avg(tall1, tall2):
    print("linje 20")
    return (tall1 + tall2) / 2

a = 3


print("linje 26")
print(avg(2, 4))
print(avg(5, 10))
print("linje 28")
#print(avg("Hei", "hu"))

text_med_linjeskift = "asdj\nhasd"
print(text_med_linjeskift)

liste = [1, 2, 3]
print(type(liste))

for element in liste:
    print(element)

print(liste[1:])
print(liste[:-1])

sannhet = False

if sannhet:
    print("det stemmer")
else:
    print("det stemmer ikke")


