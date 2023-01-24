
class Person:

    def __init__(self):
        self.married_to = None

    def marry(self, other):
        self.married_to = other
        other.married_to = self


p1 = Person()
print(id(p1))
p2 = Person()
print(id(p2))


p1.marry(p2)
print(f"{p1} er gift med {p1.married_to} og {p2} er gift med {p2.married_to}" )
p1.married_to = None
print(f"{p1} er gift med {p1.married_to} og {p2} er gift med {p2.married_to}" )



