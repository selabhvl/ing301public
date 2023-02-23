# Projekt Del B: Persistens og database

## Formål

I det andre steget av prosjektet skal vi sørge for at den informasjonen som representeres som
et objektstruktur på _runtime_ lagres permanent på en hard-disk slik at vi ikke mister noe
informasjonen når programmet blir avsluttet.

For å gjøre dette skal vi bruke det lettvekt databasesystem [SQLite](https://www.sqlite.org/index.html).

Applikasjonen fra del A skal utvides slik at
- den kan leser byggningsstrukturen og enhetsinformasjoner fra databasen,
- tilstanden til aktuatorer lagres persistent i databasen og
- man kan kjøre noen statistiske analyser og spørringer på sensormålinger.

## Setup

For å gjøre denne oppgaven kan dere jobbe direkte videre på deres eksisterende prosjekt.
Alternativ kan dere også bruke vår løsningsforslag til prosjekt del A som utgangspunkt:

[Løsningsforslag](https://github.com/selabhvl/ing301-projectpartA-solution)

Vi antar at deres prosjekt repository ser altså noenlunne slik ut (eventuelt har dere ha laget flere Python filer):
```
.
├── README.md
├── devices.py
├── main.py
├── smarthouse.py
└── smarthouse_test.py
```

Dere skal nå kopiere de tre filene som befinner seg [her](./startkode-del-b)
inn i deres repository slik den resulterende mappestrukturen ser ut som

```
.
├── README.md
├── db.sqlite                   <-- nytt
├── demohus-devices.csv
├── devices.py
├── main.py
├── persistence.py              <-- nytt
├── persistence_test.py         <-- nytt
├── smarthouse.py
└── smarthouse_test.py
```

En liten forklaring på hva disse tre nye filene gjør:
- `db.sqlite` SQLite database filen som inneholder et ferdig datasett dere skal jobbe videres med
- `peristene.py` inneholder et enkelt database grensesnitt klasse (`SmartHousePersistence`) og en klasse med analysemetoder som dere skal utvikle.
- `persistence_test.py` inneholder tester som dere kan bruke for å sjekke om alt ønsket funksjonalitet har blitt utviklet og fungerer.

Videre forventer testene at `main.py` filen inneholder en funskjon `load_demo_house()` som skal erstatte `build_demo_house()` i det lange løpet.

Dere sjak gå altså inn i `main.py` og legge inn en import på toppen
```python
from persistence import SmartHousePersistence
```
og i tillegg lage en tom `load_demo_house()` funksjon slik et valgfri sted i filen:

```python
def load_demo_house(persistence: SmartHousePersistence) -> SmartHouse:
    result = SmartHouse()
    # TODO read rooms, devices and their locations from the database
    return result
```

Dere kan sjekke at alt er satt opp riktig ved kjøre testene i `persistence_test.py`.
Når dere kjører alle testen skal ett av de seks test metodene i denne filen være _grønt_ mens de andre fem skal feile.
Dvs. hvis dere bare kjører `test_db_ok` alene skal den gi `OK`:

```
Testing started at ...
Launching unittests with arguments python -m unittest persistence_test.PersistenceTest.test_db_ok in ...

Ran 1 test in 0.003s

OK

Process finished with exit code 0
```

## Utforsk tabellen

Oppgaven deres er nå til å få alle testene å bli grønn.
Før dere begynner med koding da, kan det være lurt å utforske databasen litt i forkant.
Dere kan bruke et verktøy som [DBeaver](https://dbeaver.io/) til dette.

Når dere åpner DBeaver for første gang skal dere til venstre se et vindu som heter `Database Navigator`.
Den ligner litt på filtre "explorer".

**TIPPS**: Hvis man har rotet seg bort å forskyvet vinduene hit og dit kan man komme seg tilbake til
utgangspunktet ved å trykke på `Window` (i vindu menyen) -> `Reset Perspective`.


Gjør så en høyreklikk i `Database Navigator` og  `Create` > `Connection` i kontekstmenyen.
I det nye vinduet som kommer opp, velg `SQLite` og så `Next`.
Cursoren skulle stå i et felt som heter `Path`.
Her skal vi skrive inn filstien til `db.sqlite` filen.

For å finne filstien kan dere
- Hvis dere bruker PyCharm: I Project-Explorer ved å høyreklikke på filen og så `Copy Path / Reference` -> `Absolute Path`.
- I VS Code: Skrive `pwd` i terminalvinduet, kopiere inn den stien som blir gitt ut som resultat og setter `db.sqlite` på slutten.

Nå kan dere lime inn den stien vi nettopp hadde kopiert i DBeaver vinduet.
Hvis dere trykker på `Connection details (type, name, ...)` knappen åpnes et nytt vindu da dere kan
gi et mer dekkende navn til forbindelsen, f.eks `ING301ProjectB`.
Dere avslutte med å trykke på `Finish`.

Den nye forbindelsen dykker nå opp i `Database Navigator`.
Gør en dobbelklikk på den.
Nå skulle dere se en aktiv (dvs. den har et grønt sjekkmerke) forbindelse mot prosjektets `db.sqlite` fil.
Når dere gjør en høyreklikk på den kan dere velge `SQL Editor` > `Open SQL Script` i kontekstmenyen.
Nå velger dere `New Script` slik at et nytt editorvindu åpner seg der dere kan skrive SQL.
F.eks kunne dere skrive 
```sql
SELECT name FROM sqlite_schema WHERE type = 'table';
```
for å finne ut hva tabeller det finnes og hva de heter.

Når vi vet hvordan tabellene heter, kan dere kjøre en `SELECT` mot dem:
```sql
SELECT * FROM  rooms;
```
vil gi der romstrukturen av det demohuset dere kjenner fra første delen.

## Mål og hvordan begynner jeg

Målet er som sagt å få alle testene grønt.
Testene kan deles inn i tre grupper:

`test_loading_demo_house` tester om dere har `load_demo_house` i `main.py` riktig implementert.
Den metoden skal lese romstrukturen og enhetsinformasjonen fra databasen og bygge opp
objesktrukturen av demo huset litt sånn som dere har gjort det i `build_demo_house`.

`test_updating_sensor_state` tester at forandringer på statusen til en aktuator lagres i databasen.
F.eks. slit at databasen vet at en lyspære er slått på eller av eller hva temperatur en varmeenhet er stilt inn på.
For å realisere dette må dere kanskje utvide database strukturen: Kanskje legge til tabeller med `CREATE TABLE` eller
legge til en kolonne til en eksisterende tabell med `ALTER TABLE`.
I tillegg må `Device` (sub)klassene kanskje utvides at disse vet om deres database-relatert metainformasjon (`id`) og har en tilgang til databasen (dvs. `sqlite3.Cursor` objekter).

De resterende testene `test_analytics_easy`, `test_analytics_medium` og `test_analytics_advanced` tester
funksjonaliteten av `SmartHouseAnalytics` klassen.
Denne inneholder en del tomme funksjoner som dere skal lage innhold for.
Konkret må dere skrive et tilsvarende `SELECT` spørring.

Det kan være greit å utvikle i DBeaver først før dere legger det inn i et `cursor.execute("...")`
Spørringene tar seg gradvis opp i vanskelighetsgraden.
Akkurat det siste kan være litt "tricky", følgende ressurser kunne være hjelpsom der:

- https://www.sqlite.org/lang_datefunc.html
- https://www.w3resource.com/sql/subqueries/understanding-sql-subqueries.php
- https://www.w3schools.com/sql/sql_having.asp

Lykke til!


