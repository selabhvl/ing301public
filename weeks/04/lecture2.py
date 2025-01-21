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


tall1 = 4.7
tall2 = 8.91
print("linje 26")
print(avg(tall1, tall2))
print("linje 28")


