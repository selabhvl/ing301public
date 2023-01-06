# Python Installasjon under Mac OS X

For å installere Python og git under MacOS vi anbefaler først å installere [https://brew.sh/](https://brew.sh/)
Brew en _package manager_ som kanskje noen kjenner det fra forskjellige Linux distribusjoner.
Den gjør det svært enkelt å installere forskjellige verktøy (spesielt utviklingsverktøy).

For å få i gang brew trykk på _Launchpad_ og så søker du på _Terminal_.
I det viduet som åpner seg skriver du:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
og `<Enter>`!

Du vil eventuelt bli spurt om passordet underveis...

## Installasjon Python

Før du installere noe kan du fakstisk teste om du kanskje allerede har Python på plass ved å skrive
```bash
python3 -V
```
i Terminal og trykk på `<Enter>`. Hvis du har Python så vil gi deg den presise Python Subversion tilbake (f. eks. `Python 3.10.6`). 

Hvis ikke, så må du laste ned Python:
Skriv 
```bash
brew install python3
```
i Terminal og trykk `<Enter>`. 

## OBS!

Det er viktig å huske at når du vil kjøre Python fra kommandolinjen under MacOS så må du alltid skriver `python3` istedenfor (ved å bare `python` vil Python versjon 2 åpner seg. Og den skal vi ikke bruke lenger).


