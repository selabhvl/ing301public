# Denne Python script'en illustrerer at man må ta ekstra hensyn ift. bidirektionale assossieringer


class Person:

    counter = 1

    def __init__(self):
        self.name = f"Person {Person.counter}"
        Person.counter += 1
        self.married_to = None

    def marry(self, other):
        self.married_to = other
        other.married_to = self

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


p1 = Person()
p2 = Person()


p1.marry(p2)
print(f"{p1} er gift med {p1.married_to} og {p2} er gift med {p2.married_to}" )
# Å forandre denne variablen bare en av de to samenkoblete objekte er farlig
# siden dette skaper en inkonsistent situasjon.
# Den riktige løsningen  hadde vært å legge til en 'divorce' metode.
p1.married_to = None
print(f"{p1} er gift med {p1.married_to} og {p2} er gift med {p2.married_to}" )



