# Python Installasjon under Windows

Hvis du bruker Windows 10 og ikke har installert _Python_ er Windows sin [App Store](https://apps.microsoft.com/) den enkleste måten å skaffe seg seg _Python_. Bare følg følgende lenken:

https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5

og så klikk på _Get in Store_. Windows tar seg av resten.

I tillegg anbefales det å installere en moderne _Terminal_ grensesnitt: [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=nb-no&gl=no) er en modern versjon av det gamle `cmd.exe` og kan lastes ned i Microsoft App Store.

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

## Alternative installasjonsmåten

Hvis du ikke vil bruke App Store installasjonen, så kan du laste ned Python direkte [her](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe).
Den lenken vil laste ned en Installer.exe som vil installere Python på ditt system.

Du kan også bruke [Anaconda](https://www.anaconda.com/) for installere Python på ditt system.
Denne kommer likevel med en del ekstra kompleksitet og anbefales bare hvis du har brukt dette før!
