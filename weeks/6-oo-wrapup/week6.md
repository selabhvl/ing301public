# Uke 6: OO oppsumering

Vi skal avslutte vår eventyrreise inn i objektorientering sin verden ved å 
se på noen nyttige tekniske detaljer om hvordan Python handterer objekter internt
og hvorfor vi av og til måtte gi våre funksjoner upraktiske navn som begynner med
`__` (double underscore).

## Slots

Når du lager en ny _klasse_, la oss si at vi har kalt den for `A`, så kan
vi jo lage oss massevis av _objekter_ til denne klassen ved å skrive klassenavn følgt av paranteser.

```python
class A:
    pass  # ikke noe mer struktur her akkurat nå

obj1 = A()
obj2 = A()
obj3 = A()
# ... mange flere
```

Siden definisjonen av `A` legger veldig få føringer, så er `A`-objektene relativt blank:
I utgangspunkt kan disse bare brukes som et slags Python _ordbok_ (`dict`).
Istedenfor å bruke ordbøkene sine indeks-notasjon (`dict[key]`) så kan vi bruke _punkt-notasjonen_ (`obj.key`) på disse:

```python
obj1.name = "Alice"
obj2.name = "Bob"
print(obj1.name)
```

Internt bruker Python faktisk en ordbok til å representere disse egenskapene.
Punkt-notasjonen er altså bare en slags _syntaktisk sukker_.
Dvs. at den første linjen i kodeeksemplet ovenfor egentlig tilsvarer:
```python
obj1.__dict__['name'] = "Alice"
```

Denne måten å bruke klasser på er veldig fleksibelt men samtiding også noenlunne _usikker_.
Som du ser så har `obj3` i kodeeksemplet ovenfor ikke fått tildelt egenskapet `name`.
Hvis en senere bruker av vår kode nå hadde stolt på at alle `A`-objekte har denne egenskapen
så vil det komme litt overraskende på. I tillegg kan `A`-objekte jo tildeles all slags 
egenskaper. Men ofte er jo selve hensikten ved å lage en klasse jo akkurat det å karakterisere
en viss mengde av objekte som er "_likt_" på et vis. 

Hvis vi altså ville si at alle `A`-objekter har et `name`-attributt og bare det så kan man definere en **klassevariable** 
med navn `__slots__` som er en liste av attributtnavn:

```python
class A:
    __slots__ = ["name"]

obj1 = A()
obj1.name = "Alice"
obj1.age = 42  # Dette er ikke lov lenger og vil gi en Error!
```


## Abstrakte Metoder

I forrige uke har vi sett på noen programvareutviklings designmønstre som baserer seg at det finnes en slags
_abstrakt_ klasse på toppen som definerer noen funksjoner (legge føringer) som potensielle subklasser kan implementere.
I et eksempel er _Visitor_.

```python
# Begynnelsen av en komplekst hierarki
class Visitor:
    def handle_B(self, b_objekt):
        pass  # Abstrakt

    def handle_C(self, c_objekt):
        pass  # Abstrakt


class A:
    def accept(self, visitor: Visitor):
        pass  # Abstrakt


class B(A):
    def accept(self, visitor: Visitor):
        visitor.handle_B(self)


class C(A):
    def accept(self, visitor: Visitor):
        visitor.handle_C(self)
```
Hvis noen eksterne vil bruke denne koden og definere forskjellige oppførsel basert på
den konkrete typen av en `A`-subklasse-objekt så kan hen bare lage en subklasser av `Visitor`
og implementere `handle_X`-funksjonene. 
Men hva hvis typhierakiet under `A` blir utvidet med nye klasse. 
Da må jo legges til nye `accept` og `handle` metoder?!
Dette er jo lett å glømme! 

Python er mindre streng vedrørende sjekk av din kode sammeligned med andre språk.
Dette har både fordeler og ulemper. Men du kan tvinge Python til å være mer streng her
ved bruk av noe som heter `abstractmethod` som befinner seg i modul `abc`.
```python
from abc import abstractmethod

class Visitor:
    @abstractmethod
    def handle_B(self, b_objekt):
        pass  # Abstrakt
    
    @abstractmethod
    def handle_C(self, c_objekt):
        pass  # Abstrakt


class A:
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass  # Abstrakt


class B(A):
    def accept(self, visitor: Visitor):
        visitor.handle_B(self)


class C(A):
    def accept(self, visitor: Visitor):
        visitor.handle_C(self)
```
I kodeeksemplet ovenfor har vi lagt til `@abstractmethod` som er en _Dekorator_.
Denne skrives foran funksjonsdefinisjoner og vil tvinge mulige framtidige subklasse av `A` og implementere `accept` 
og subklasser av `Visitor` begge `handle` metodene.

## Magiske Metoder

## Type Hints

## Høyre ordens funksjoner

## Moduler og Paketer


