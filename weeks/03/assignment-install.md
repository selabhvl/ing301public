# Oppgave 1 - Installasjon av utviklingsmiljø

Målet med denne første _obligatoriske_ oppgave er å sikre at alle har et fungerende utviklingsmiljø for Python programmering og kunne dele koden med andre via versjoneringssystemet _git_.

Innleveringsfrist: se Canvas.

## Steg 1: Installere verktøy

Før vi begynner må vi være sikre på at dere alle har installert verktøyene som trengs for programvareutvikling med Python

Det vil si at du må ha
- Selve [Python](https://www.python.org/) fortolkeren sammen med sitt standardbibliotek. Hvis du har allerede installert Python på din maskin, sjekk at du har installert en versjon som er nyere er likt 3.12
- En [git](https://git-scm.com/)-klient for samarbeid og deling av kode. Mest sannsynligvis vil du også en grafisk klient som f.eks. [GitHub Desktop](https://desktop.github.com/download/) hvis du ikke vil bruke `git` direkte fra kommandolinjen.
- Et integrert utviklingsmiljø (som også kalles for _IDE_ = "Integrated Development Environment"). Vi anbefaler enten [Visual Studio Code](https://code.visualstudio.com/) eller [PyCharm](https://www.jetbrains.com/pycharm/)

Lenker til instruksjoner for de enkelte operativsystemer finder du nedenfor:

### Windows

- [Python Installasjon](install_python_windows.md)

- [Git Installasjon](install_git_windows.md)

### Mac OS 

- [Python Installasjon](install_python_mac.md)

- [Git Installasjon](install_git_mac.md)

### Linux

- [Python Installasjon](install_python_linux.md)

- [Git Installasjon](install_git_linux.md)

### IDE og andre grafiske verktøy

OBS! Det er fult mulig å skrive kode i Python i en teksteditor som `vim` eller `emacs` og betjene `git` gjennom kommandolinjen (Windows sitt _Notepad_ anbefales derimot ikke i det hele tatt). 
Men generelt anbefaler vi at du bruker en IDE og/eller andre verktøy som tilbyr en grafisk brukergrensesnitt (GUI) for å gjøre det enklere!

Instruksjoner på hvordan du setter opp disse verktøy for ditt operativsystem finner du bak de enkelte Download-lenker.
I de fleste tilfeller vil du få en slags _Installer_ som gjør selve oppsett ganske enkelt.

Som nevnt før, av integret utviklingsmiljø anbefales:

- [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)

- [Visual Studio Code](https://code.visualstudio.com/)

og som grafisk klient for git/GitHub:

- [GitHub for Desktop](https://desktop.github.com/)

Hovedforskjellen mellom PyCharm og VS Code er at førstnevnte krever en lisens (du får det gratis som student ved HVL) og er litt tyngre å kjøre, samtidig har den mer funksjonaliteter og støtte enn VS Code. VS Code f.eks har i utgangspunkt ikke støtte for Python utvikling, du må installere [en 'extension'](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for dette.

## Steg 2: Lage GitHub bruker 

Vi skal bruke sky-tjenesten [GitHub](https://github.com)] for å dele eksempel kode for forelesninger og for at dere kan jobbe sammen i grupper om programmering. Du trenger derfor en bruker på github. Om du allerede har en github brukerkonto kan du hoppe direkte til neste steg.

Først, gå til https://github.com/ i din nettleser! På hovedsiden trykker du nå på _Sign Up_. Du blir bedt til å gi fra deg en epost adresse (Du kan bruke din HVL-epost-adresse) og sette et password. Pass på at lagrer dine pålogginsinformasjon på et sikkert sted (f.eks. ved å bruke en _Password Manager_).

## Steg 3: Clone ing301public oppbevaringsplassen

Vi skal bruke oppbevaringsplassen  

> <https://github.com/selabhvl/ing301public>

for kode-eksempler fra forelesninger og annen informasjon.

Sjekk at du er logget på GitHub og åpne gitt URL i din nettleser.

Oppe til høyre finner du en grønn knapp `Code`. Trykk på den og kopier den URLen du ser i den dialogen som åpner seg.

Lag nå en _mappe_ på din harddisk bak en filsti som er lett å huske, f.eks. `C:\Users\<dinbrukernavn>\ING301\` (eller `/home/<dinbrukernavn>/ING301/` på Linux/Mac). 
I neste steg kan du åpne et _terminal_ vindu og navigere deg til samme filstien ved å bruke `cd` (kommandoen for *change directory*).

**VIKTIG**: *ikke* velg en mappe som er tilkoblet til fildelingstjeneste som OneDrive eller Dropbox. Det kan gi problemer med git og IDE senere.

Du kloner et repository ved å utføre følgende kommando i terminalvinduet:

```bash
git clone https://github.com/selabhvl/ing301public
```

Repositoriet vil bli oppdatert i løpet av kurset. For å få med deg de siste oppdateringene kan du bruke:

```bash
git pull 
```

Hvis du har valgt å installere GitHub Desktop applikasjonen kan du også bruke denne til å klone oppbevaringsplassen (vises i forelesningen).

## Steg 4: Skrive og teste Python kode

Til slutt skal vi teste om din Python installasjon virker som den skal.
Du skal nå åpne din IDE og så åpne `ing301public` mappen i den (i VS Code finner du en knapp "open folder" og i PyCharm finner du en knapp "open project").
Når du åpner mappen kommer et spørsmål om du stoler på innholdet: her sier du bare "ja" :wink:.
Etterå kan du navigere til filen `/weeks/03/testinstall.py` i filtræet på venstresiden og kjører den ved å trykke på den _store grønne knappen_.
Du burde da se noe som:

```
Congratulations 🎉 It looks like you are running Python in version 3.12 and ready for ING301 - Spring'NN 🎓 !!!

BTW did you know that...
[...]
```

som indikerer at oppsett av utvklingsmiljø var en suksess!
