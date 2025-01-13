# Python Installasjon under Windows


Python er et svært populært programmeringsspråk.
Dette medfører at det finnes mange forskjellige måter å få Python siden Python integreres i forskjellige programvarer.
Et resultat av dette er desverre at det kan være litt forvirrende om hvordan man setter opp Python på en bra måte.

Som et referanse med mange tekniske detaljer om oppsett og bruk av Python under Windows, anbefaler vi å ta en kikk [i den offisielle guiden](https://docs.python.org/3/using/windows.html)!

Noen måter å installere Python på:
- Bruk av [den offisielle _Installer_'en](https://docs.python.org/3/using/windows.html#the-full-installer)
- gjennom Windows sin [App Store](https://apps.microsoft.com/)
- gjennom [Anaconda](https://www.anaconda.com/download)
- gjennom [nuget.org](https://www.anaconda.com/download)

## Python installer 

Vi anbefaler første alternative, altså gjennom Python Installer.
Du kan laste filen ned [her](https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe).
Når .exe filen er lastet ned, kan du utføre den (forutsetter at du har kontroll over datamaskinen din og ikke at den er forvaltet av en forretning eller lignende. Stikkordet: "no group policies!").

![Python Installer Screenhsot](https://docs.python.org/3/_images/win_installer.png)

Du kan bare installere med standardinstillinger ved å trykke på "Install Now", men vi anbefer at du 

- ta vekk krysset ved "Install Lancher for all users"
- sett krysset ved "Add Ptyhon 3.XX to PATH"


Hvis du er på Windows 10, anbefales det i tillegg å installere en moderne _Terminal_ grensesnitt: [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=nb-no&gl=no) er en modern versjon av det gamle `cmd.exe` og kan lastes ned i Microsoft App Store i Windows 10, mens i Windows 11 er det allerede installert fra begynnelsen.

Når du installert begge deler, prøv å åpne Windows Terminal fra _Start_-menyen og så skriver du 

```bash
python
```


Du vil da komme inn i den interaktive _Python_-interpreteren. Du kan teste den ved f. eks. gi dem en regneoppgave:
```
>>> 2 + 3
```

som vil forhåpentligvis vil gi deg svaret `5`. Hvis du vil avslutte, så skriver du

```
>>> quit()
```

Da skal du være tilbake i det vanlige Terminalet.
Grattis! Nå er du du klar til å utvikle med Python!
Vi anbefaler likevel at du laster ned [Visual Studio Code](https://code.visualstudio.com/) eller [JetBrains PyCharm](https://www.jetbrains.com/pycharm/).


