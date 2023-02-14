# Uke 7: Databaser Intro

Denne uken skal vi begynne å se litt nærmere på _databasesystemer_ (eller _database manegement systems (DBMS)_ som man kaller dem på engelsk).
Motivasjonen til det hele er at vi vil gjerne lage data som oppstår i et program på runtimer utøver "livstiden" til selve programmet.
Det hele kalles ofte for _persistens_.

Den ekleste måten å lagre data persistent er å bruke filer.
Python sin standardbibliotek kommer med en innebygget funksjon:
```python
fil = open("./path/file.end", "rw", encoding="UTF-8", newline="\n")
```
vil gi deg en objekt av type `io.StringIO` som gjør det mulig å lese innholdet av en fil som tekst (`str`) linje for linje (`fil.readlines()`) også legge til tekst på slutten (`fil.writelines()`).
Ulempen med filer deres realtivt lave abstraksjonsnivå:
Når en jobber med filer må man tenke på mange aspekter som
- Backup (i tilfelle systemfeil)
- Tilgansstyring, Rettigheter, ...
- Encodings
- og hvordan datastrukturer oversettes til sekvenser av bytes (serialisering).

Databaser tilbyr et høyere abstraksjonsnivå slik at man ikke må bry seg om disse tekniske aspektene.
I forelesningen skal vi bruke `sqlite` som er et slags lettvekt databasesystem som har direkt støtte i Python sin standardbibliotek.


```python
from sqlite3 import Connection
conn = Connection("dbfile.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT * FROM tabell")
results = cursor.fetchall()
for result in results:
    print(result)
cursor.close()
```


Mer rundt dette kommer i forelesningen...