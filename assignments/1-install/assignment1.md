# Oppgave 1 - Installasjon av utviklingsmiljø

Målet med denne første _obligatoriske_ oppgave er å sikre at alle har et fungerende utviklingsmiljø for Python programmering og dele koden med andre.

Innleveringsfrist: se Canvas.

## Steg 1: Installere verktøy

Før vi begynner må vi være sikre på at dere alle har installert verktøyene som trengs for programvareutvikling med Python

Det vil si
- [Python](https://www.python.org/) fortolkeren og standard biblioteker. Hvis du har allerede installert Python på din maskin, sjekk at den har et versjonsnummer som begynner på _3_!
- Klient for [Git](https://git-scm.com/) versjoneringssystemet for samarbeid og deling av kode 
- Et integrert utviklingsmiljø for Python

Lenker til installasjonsinstruksjoner for de forsjellige operativsystemer finder du nedenfor

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

Det er fult mulig å skrive kode i Python i en teksteditor som `vim` eller `emacs` og betjene git gjennom kommandolinjen (Windows sitt _Notepad_ anbefales derimot ikke i det hele tatt). 
Men generelt anbefaler vi at du bruker en IDE og/eller andre verktøy som tilbyr en grafisk brukergrensesnitt (GUI).

Som integret utviklingsmiljø anbefales:

- [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)

- [Visual Studio Code](https://code.visualstudio.com/)

og som grafisk klient for git/GitHub:

- [GitHub for Desktop](https://desktop.github.com/)

## Steg 2: Lage GitHub bruker 

Vi skal bruke sky-tjenesten [GitHub](https://github.com)] for å dele eksempel kode for forelesninger og for at dere kan jobbe sammen i grupper om programmering. Du trenger derfor en bruker på github. Om du allerede har en github brukerkonto kan du hoppe direkte til neste steg.

Først, gå til https://github.com/ i din nettleser! På hovedsiden trykker du nå på _Sign Up_. Du blir bedt til å gi fra deg en epost adresse (Du kan bruke din HVL-epost-adresse) og sette et password. Pass på at lagrer dine pålogginsinformasjon på et sikkert sted (f.eks. ved å bruke en _Password Manager_).

## Steg 3: Clone ing301public oppbevaringsplassen

Vi skal bruke oppbevaringsplassen  https://github.com/selabhvl/ing301public for kode-eksempler fra forelesninger og annen informasjon knyttet til Python programmering.

Sjekk at du er logget på GitHub og besøk: https://github.com/selabhvl/ing301public

Oppe til høyre finner du en grønn knapp `Code`. Trykk på den og kopier den URLen du ser i den dialogen som åpner seg.

Lag nå en mappe på din harddisk på filsti som er lett å huske, f.eks. `C:\Users\<dinbrukernavn>\ING301\` (eller `/home/<dinbrukernavn>/ING301/` på Linux/Mac). 
Åpner en _Terminal vindu_ og navigere til denne filstien.

Nå er det på tide å clone ING301 repo'en. Bruke følgende kommando:
```bash
git clone <Github URL du har kopiert tidligere>
```

Oppbevaringsplassen https://github.com/selabhvl/ing301public vil bli oppdatert etterhvert utover semestret. For å oppdatere din lokale kopi bruk:

```bash
git pull 
```

i mappen der din lokale kopi av oppbevaringsplassen ligger.
 
## Steg 4: Skrive og teste Python kode

Nå er det på tide å sette i gang for fult! Vi skal skrive vår første kode i ING301!

Forutsetningen er at du har klart å sjekke ut en lokal kopi av `ing301public`. 

Du skal nå åpne denne `ing301public`-mappen i en IDE:

**VS Code**
```
File > Open Folder ... > (navigate to the ing301public folder on your disk) > "Yes, I trust the authors"
```

**PyCharm**
```
File > Open > (navigate to the ing301public folder on your disk) > Trust Project > This Window (if you are asked)
```

Uansett hvilken IDE du bruker skal du på venstre siden se "filtræet" med selve `ing301public` mappen som øverste nivå.
 
I dette træet navigere ned til `assignments/1-install/testinstall.py`. 
Både VS Code og PyCharm tilbyr en mulighet til å direkte "kjøre" filen fra editoren (_Bare trykk på den "Spill av" knappen_).
Alternativt kan du kjøre filen fra en _Terminal_ slikt:
```
python3 <filsti her>/assignments/1-install/testinstall.py
```

som resultat skulle du se noe slikt:
```
Congratulations you are running Python in version 3....
[Clang ..............]
and also your repository layout looks alright!
```

Dette betyr at du har klart til å laste ned startkoden gjennom `git` og at din maskin er klar til å skrive og kjøre Python kode! 
