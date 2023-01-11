# Python 


Denne siden er tenkt som veldig kjapt innføring repetisjon av sentrale elementer i Python programmeringsspråket. 
Noen konsepter er omskrevet veldig grovt og vi viser til forskjellige kapitler i boken _Practical Programming_.
Vi anbefaler derfor at du supplerer denne teksten her med andre ressurser, f.eks.:


- [Python Lærepgrogram på W3Schools](https://www.w3schools.com/python/)
- [Python Standard Bibliotek Oversikt](https://docs.python.org/3/library/index.html)
- [Det offisielle Python Lærepgrogram](https://docs.python.org/3/tutorial/index.html)
- også vil du sannsynligvis finne masse andre Python læreprogram...

## Utføre Python kode

Python er en _tolket_ programmeringsspråk. 
Det vil si at en spesiell program: _fortolkeren_ (engl. interpreter) leser inn instruksjonene og utføre tilsvarende kommandoer.


Når du har installert Python kan du åpne fortolkeren ved å åpne en Terminal og skriver
```bash
> python
```
hvis du er på Windows, eller 
```bash
$ python3
```
hvis du er på Linux eller Mac.

Fortolkeren leser en kommando om gangen, evaluere den, og så gi deg resultatet tilbake:
```
Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> print("Hei verden")
Hei verden
>>> import math
>>> math.sqrt(9)
3.0
>>> quit()
```

Som su ser kan du avslutte fortolkeren ved å skrive `quit()`.

Det å utvikle større programmer direkte i fortolkeren kan rask bli svært uoversiktlig. 
Derfor skriver man Python kode vanligvis i filer. 
En slik fil blir kalt _Script_. 
En Skript er en vanlig tekstfil med et navn som slutter på `.py` og inneholder en sekvens av Python kommandoer.


## Uttrykk

Vi anbefaler nå at du åpner opp din favoritt teksteditor elle ennå bedre: en IDE som _PyCharm_ eller _VS Code_.
For å følge med, lag en ny Python fil med valgfri navn (f.eks.`firststeps.py`) og åpner den file i editoren. 
Til å begynne, kan du prøve deg på det [det programmet](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) som var grunnlag for mange utviklerkarrierer:

```python
print("Hello, World!")
```
Du kan kjøre denne koden ved å skrive
```bash
$ python firststeps.py  # python3 under Linux/Mac
```
i Terminal eller hvis du bruker en IDE kan du kjøre file direkte fra teksteditor vinduet.

For å forklare litt mer om hva du nettopp har laget:

- Du har skrevet din første Python script som består an en enkelt kommando
- Kommandoen kaller den [innbyggete funksjonen](https://docs.python.org/3/library/functions.html) `print()`
- `print`-funksjonen har et argument (det som står i parenteser), nemlig en tekst (`"Hello, World!"`).
- Effekten av å kalle funksjonen er at den skriver ut argumentet på [standard out](https://en.wikipedia.org/wiki/Standard_streams#Standard_output_(stdout)), altså det som kommer tilbake fra kommandolinjen.

Framover skal vi bruke `print()` veldig ofte for å vise hva som foregår i våres programmer.

La oss nå også overføre den beregningen vi hadde gjort direkte i fortolkeren inn i vår ny script fil.
```python
print("Hello, World!")
2 + 3
```
Hva skjer hvis du kjører filen nå?

Savner du noe?


Det er fordi når du kjører en hel fil med fortolkeren så vil hele file utført som ett men uten at du blir informert over alle resultater som oppstår inn i mellom. 
Uttrykket `2 + 3` beskriver en operasjon (addisjon) mellom to heltall verdier. 
Når dette uttrykket blir "kjørt" så blir den evaluert, noe som produserer et nytt heltall (5). 
Men siden vi gjør ikke noe mer med det, så forsvinner resultatet bare uten effekt. 
For å bruke det videre må vi enten bruke det direkte i en funksjon eller vi lagrer resultatet i en _variable_ for å kunne bruke det senere.

```python
print("Hello, World!")
2 + 3  # beregne et uttrykk, men uten å lagre resultatet => ingen effekt
print(2 - 3)  # beregne et uttrykk og gi det til print() funksjonen
x = 2 * 3  # igjen beregne et uttrykk, men denne gangen lagret i en variable
print(x)  # bruke variabelen
```

## Variable og Datatyper

Uten å nevne det eksplisitt har vi allerede brukt forskjellige Python datatyper: 
Vi har brukt forskjellige tall: `2`, `3` og en kort tekst: `"Hello, World!"`. 
Alle har til felles at de representerer faste _verdier_. 
I programmeringsspråk sin verden så kaller men disse ofte for _konstanter_.

Men hvorfor kunne vi skrive direkte skrive `2` men får skrive en tekst så måtte vi bruke `""` rundt?! 
Det er fordi de har forskjellige typer! 
Kanskje du husker når realfaglæreren maste med hvilket enhet når hen spurte etter lengde, hastighet, kraft ... 
Like som du ikke kan bare plusse på en hastighet med en elektrisk spenning så har verdier i programmeringsspråk forskjellige _"enheter"_, eller _typer_ som vi kaller dem.

Heldigvis er mengden av disse elementære typene relativt liten.
I Python finnes det:
- Tekst, dvs. en sekvens av tegn (engl. characters) som avgrenses med en innledende `"` og en avsluttende `"` (alternativt kan du bruke `''`). På engelsk kalles denne typen ofte for _string_ og i Python heter den `str`.
- Heltall (som kan være positivt eller negativt), På engelsk kaller man dem for _integer_ og i Python heter de `int`.
- Kommatall (men istedenfor komma så bruker man en desimalpunkt `.` => amerikansk skrivemåte), På engelsk kaller man dem for _floating point numbers_ og i Python heter de `float`.
- Sannhetsverdi: Det finnes akkurat to sannhetsverdier: `True` og `False`. På engelsk kalles dem _boolean values_ og i Python heter de `bool`.

Prøv å utvide ditt program med følgende linjer:

```python
heltall = 42
kommatall = 3.1415296
tekst = "Hallooooooo"
sannhet = True

print(type(heltall))
print(type(kommatall))
print(type(tekst))
print(type(sannhet))
```

Som du ser har vi innført en ny innbygget funksjon (`type()`) som du kan bruke å finne ut hva som er typen til en konstante eller variable skulle du være usikker.

Avhengig av typen, finnes det forskjelligere operatorer og funksjoner som kan brukes. 
Legg til følgende operasjoner og prøv å gjette hva som vil bli returnert av programmet før du kjører den.

```python
print(heltall - 1)
print(kommatall ** 2)
print(tekst * 3)
print(not sannhet)
```



### Numeriske operasjoner

Typer som representerer tall, dvs. `int` og `float` støtter all de numeriske operasjonene som du kjenner fra før
```python
99 + 1  # addisjon
42 - 1  # subtraksjon
2 * 3  # multiplikasjon
2 / 3  # divisjon
2 ** 6  # eksponent
```
Vær oppmerksom på at resultat av en divisjon alltid vil gi deg et kommatall (`float`).
Det gjelder også når begge inputt tall er heltall og divisjonen går opp uten rest.
```python
resultat = 4 / 2 
print(resultat)  # 2.0
print(type(resultat))
```
Også, når du anvender en operasjon av et heltall og et kommatall så vil du få et kommatall tilbake.
Hvis du er derimot interessert i heltall divisjon så bruker du `//`.
Denne operasjonen kommer i lag med en operasjon som heter _modulo_ (`%`) som gir deg den mulige resten som kan oppstår i divisjonen:
```python
# 7 delt med 3 blir 2 med rest 1 (7 == 2 * 3 + 1)
7 // 3  # == 2
7 % 3  # == 1
```

Vi anbefaler at du leser kapittel 2 (_"Hello, Python"_) i boken _Practical Programming_ som oppsummering av det vi har gjort så langt.

### String operasjoner
Tekster tilbyr også noen operasjoner som ser akkurat likt ut som de numeriske operasjonene men oppførelsen deres skiller seg vesentlig.

```python
"Hallo" + ", " + "verden"  # limer flere tekster sammen
"Hei!" * 3  # Gjentar en tekst flere ganger
```

Vi skal komme tilbake til `str` typen lenger nede når vi snakker om funksjoner og lister.
Hvis du allerede nå vil lese mer om operasjoner på string så anbefaler vi lesing i kapittel 4 (_"Working with Text"_) i _Practical Programming_.

### Boolske operasjoner

Den sannhetsverdi datatypen `bool` tilbyr tre operasjoner: `and`, `or` og `not`.
Oppførelsen til disse operasjoner kan beskrives med _sannhetstabeller_:

#### `and`
Venstre | Høyre   | Resultat
------|---------|----------
`False` | `False` | `False`
`False` | `True`  | `False`
`True`  | `False` | `False`
`True`  | `True`  | `True`

#### `or`

Venstre | Høyre    | Resultat
------|---------|----------
`False` | `False` | `False`
`False` | `True`  | `True`
`True`  | `False` | `True`
`True`  | `True`  | `True`

Som man ser gi `and` tilbake `True` bare hvis begge argumenter er `True` mens for `or` holder det hvis bare et argument er `True`.
Operatoren `not` anvendes på kun ett argument og gjør `True` om til `False` og omvendt.

```python
print(True and False)
print(True or False)
print(not True)
```

Sannhetsverdi brukes generelt i sammenheng med avgjørelser (`if-then-else`) og løkker (`while`).
Som vi vil snakke om om litt.
Du kan lese mer om sannhetsverdier i Kapittel 5 (_"Making choices"_) i _Practical Programming_.

### Sammenligninger

Du kan få deg en `bool`-konstante ved å skrive `True` eller `False` direkte.
Men som vanlig vil du ikke bruke disse konstanter direkte men heller "beregne" dem:
Sannhetsverdier er nemlig som oftest et resultat av en sammenligning!
I Python finnes det mange måter å skrive ned sammenligninger:

```python
2 == 2.0  # er to elementer lik
1.33 != 1.333  # er to elementer IKKE lik
1.9 <= 2  # mindre eller lik
1 < 1  # mindre
2 >= 1  # større eller lik
42 > 23  # større
```

Du kan faktisk også sammenligner tekst.
Hva tenkter du kommer ut i følgende program:
```python
print("Hei" <= "Hallo")  # True eller False ?
```
Hvis resultatet ikke skulle virker intuitivt kan du lese mer om det som kalles "[lexicografisk orden](https://en.wikipedia.org/wiki/Lexicographic_order)".

### OBS! med operasjoner

Til slutt noen advarende ord om bruk:
Du må nemlig være oppmerksom når du anvender dem på argumenter med forskjellige typer er:
```python
print(tekst + heltall)  # Dette går ikke
```
Kanskje du har også sett at noen operasjoner forandrer typen underveis
```python
print(type(heltall))
print(type(3))
print(type(heltall / 3))
```

Heldigvis kan typer ofte "transformeres":
Nesten alt kan gjøres om til tekst. Og av og til kan et tekst blir til tall (hvis den bare inneholder sifrer).
```python
print(type(str(kommatall)))
print(type(int("13")))
print(type(int("dettegårikkean")))  # Det vil ikke gå
```

## Funksjoner 

Ved siden av operatorer (+, *, /, //, %, **) finnes det funksjoner  som gjenkjennes gjennom bruken av parenteser `(...)`.
Det finnes en funksjon som du alt har brukt masse fram til nå: `print()`
Også har vi brukt `type()`, `str()`, `int()` for å finne ut mer om typen eller for å transformere typer.

Her kommer noen eksempler av slike _"innebygget funksjoner"_:
```python
lengde = len(tekst)  # lengde av en tekst
print(lengde)

print(round(kommatall, 2))  # runder ned et tall

print(abs(-5))  # fjerner et mulig minus tegn fra et tall
```

Du kan definere dine egne funksjoner slik:
```python
def hils_paa(fornavn, etternavn):
    print("Hei " + fornavn + " " + etternavn + "!")
    print("Hvordan har du det?")
```
En definisjon innledes av det reserverte nøkkelordet `def`.
Etterpå må du gi din funksjon ett navn følgt av parenteser.
I parentesene kan du definere funksjonsargumenter (Du kan definere flere ved å bruke `, `).
Argumenter kan brukes som variable i selve funksjonsinnholdet.
Etter parentesene følger det en kolon (`:`). 
Nå kan du definere alt det din funksjon skal gjøre. 
Du skriver altså Python uttrykk.
Det er viktig at du skriver fire innledende tomroms tegn i hver linje som tilhører funksjonen.
Python er nemlig et språk som bruker [signifant whitespace](https://en.wikipedia.org/wiki/Off-side_rule) for å gjenkjenne _blokker_.
Et blokk er flere kodelinjer som hører sammen.

Du kan kalle din nye funksjon rett etterpå med
```python
hils_paa("Lars", "Kristensen")
```

Du kan lese mer om funksjoner i kapittel 3 (_"Designing and Using Functions"_) i _Practical Programming_.

## Kontrollstrukturer

Ofte vil du gjøre visse ting avhengig av en betingelse.
Det er her en bruker en kjent programmeringsspråk struktur som heter `if-then-else`.

```python
klokeslett = 6  # kl 6 på morningen
if klokeslett < 7:
    print("Sov videre!")
else:
    print("Tid til å stå opp!")
```

Dette kodeeksemplet viser hvordan du skriver `if-then-else` i Python.
Den ledes inn med `if` fulgt av en _betingelse_, dvs. et uttrykk som resultere i en sannhetsverdi.
Etterpå kommer det en kolon og så definerer du en blokk med kode (akkurat som i en funksjonsdefinisjon: altså bruker 4 tomrom) som skal utføres hvis betingelsen er sant.
Du kan også legge til en `else` part med kode som skal kjøres hvis betingelsen er ikke sant.

## Lister og Løkker

Når du vil skrive programmer for å løse problemer i den ekte verden må man stort sett handtere mye data på en gang.
I Python kan du jobbe med en mengde av verdier ved å bruke lister.
```python
arbeidsdager = ["Ma", "Ti", "On", "To", "Fr"]  # Lager en liste ved å nevne elementer
wednesday_my_dudes = arbeidsdager[2]  # tilgang til enkelte elementer gjennom indeks
problem_day = arbeidsdager[0]  # Python begynner å telle på 0
nesten_helg = arbeidsdager[-1]  # man kan også telle fra slutten
```
En liste defineres ved å bruke firkantbrakett (`[ ...]`).
Listelementer skrives mellom dem skilt med `, `.
For å komme seg til et enkelt element i en liste kan du bruker indekser, dvs. posisjonsnummeret til et element i listen.
Her er det viktig å tenke på at Python begynner tellingen på `0` og ikke `1`!

Tekster (`str` verdier) oppfører seg veldig lik som lister:
```python
tekst = "hallo"
bokstav = tekst[1]
print(bokstav)
```

Lister brukes ofte i forbindelse med noe som kalles `for`-løkker:
```python
for dag in arbeidsdager:
    print(dag)
```
Løkker er brukt til å repetere kodeblokker. 
En `for`-løkke går gjennom en liste å repetere koden for hvert element i listen.
I dette tilfelle vil den skrive ut alle dagene.

Det finnes også en annen type løkke: `while`.
Som har følgende format:
```
while <betingelse>:
    <blokk>
```
Den repeterer kodeblokken så lenge betingelsen er sant.

`while`-løkker er mer fleksibelt en `for`-løkker.
I tillegg kan man gjenskape en oppførelse av `for`-løkker gjennom while løkker:

```python
i = 0
while i < len(arbeidsdager):
    dag = arbeidsdager[i]
    print(dag)
    i += 1
```

Du kan lese mer om funksjoner i kapittel 8 (_"Storing Collections of Data Using Lists"_) og mer om løkker
i kapittel 9 (_"Repeating Code Using Loops"_) av _Practical Programming_.

## Alternativer til Lister

Istedenfor lister kunne du også bruke _tupler_.
Overfladisk ser tupler akkurat likt ut som lister (sett bort fra at de skrives med vanlige parenteser)
```python
skandinavia = ('Norge', 'Danmark', 'Sverige')
norge = skandinavia[0]  # Tilgang til elementer fungerer likt
```
Den store forskjellen til en liste er at tupler **kan ikke endres** med en gang de er kreert.
Det betyr at følgende kode vil slå feil
```python
skandinavia[1] = 'Island'
```

En annen viktig datatype som hjelper med å jobbe med samlinger av verdier er _ordbok_ eller _dictionaries_ som de heter på engels.
En dictionary eller kort `dict` som Python kaller den, er en liste av `nøkkel: verdi` parer.
En `dict` defineres ved bruk av krøllparenteser (`{ ... }`).
```python
pronomener = {'Oslo': 'Jeg', 'Bergen': 'Eg', 'Trondheim': 'Æ'}
```

Du kan få tilgang til verdi elementene ved å bruke nøkkelen:
```python
print("I Bergen sier man " + pronomener['Bergen'])
print(pronomener[0])  # Dette stemmer fra lister og fungerer ikke for dict
```

`dict` objekter tilbyr noen spesielle funksjoner `.keys()`, `values()`, `.items()` som kan brukes til å utforske dem:

```python
for key in pronomener.keys():
    print(pronomener[key] + " er fra " + key)
    
for value in pronomener.values():
    print(value)
    
for noekkel_verdi_par in pronomener.items():
    print(type(noekkel_verdi_par))
```

Teoretisk kunne man en altså oppfatte en liste som en `dict` der nøklene er tall begynnende fra `0`.
```python
frukt_list = ['epler', 'banan', 'pærer']

frukt_dict = {1: 'banan', 0: 'epler', 2: 'pærer'}

for i in range(0, 3):
    print(frukt_list[i] == frukt_dict[i])
```

Du kan lese mer om tupler og ordbok i kapittel 11 (_"Storing Data Using Other Collection Types"_) i _Practical Programming_.

## Filer
Til syvende og sist må vi kort snakke om _filer_.
Filer er den primære måten å lagre informasjon i en datamaskin.
Python tilbyr funksjoner for å _lese fra_ filer og _skrive til_ filer.

```python
file = open('ing301public/week2-introduction/week2.md', 'r')  # Du kan tilpasse filstien til en fil på din maskin
for line in file:
    print(line)  # skriver ut alle linjer i en gitt fil
file.close()  # Du skulle ikke glemme denne linjen fo å unngå _Memory Leaks_
```
Denne koden viser hvordan du kan bruken funksjonen `open()` til å lese fra en fil.

```python
file = open('arbeidsdager.txt', 'w')
for dag in arbeidsdager:
    file.write(dag + "\n")
file.close()
```
og denne koden viser hvordan du kan bruke `open()` til å skrive til en fil.

Du kan lese mer om filer i kapittel 10 (_"Reading and Writing Files"_) i _Practical Programming_.
