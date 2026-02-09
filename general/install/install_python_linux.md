# Python Installasjon under Linux

Denne installasjonsinstruks baserer seg på Linux distribusjonen _Ubuntu_ siden denne er vel det mest populære.
Hvis du bruker en annen distribusjon (som _ArchLinux_, _CentOS_, _Debian_) vi antar at vil ikke ha noe problemer i å installere _git_ eller _python_:stuck_out_tongue_winking_eye:

## Python i Ubuntu

Python er faktisk allerede en del av hver fersk Ubuntu installasjon. 
Det som er viktig å huske er at i tilfelle Ubuntu Python kjøres med kommando `python3` (Hvis du skriver `python` så vil faktisk Python v.2. åpner seg!).
Du kan teste om alt er korrekt ved å åpne en Terminal vindu og så skriver
```bash
python3 -V
```
som vil gi deg informasjon hvilken underversjon av Python 3 du bruker.
Hvis kommandoen ovenfor skulle feile, så kan du etterinstallere Python med

```bash
sudo apt-get install python3 
```


## Pyenv

Du vil kanskje legge merke til at den Python versjonen som kommer med operativsystemets package manger kan bli litt utdatert i forhold til de mest aktuelle Python versjonene. I tillegg er en Python installasjon som er forvaltet av operativsystemet litt mer "ufleksibel" mtp. installasjon av fremmedkomponenter (Python Packages fra PyPI). Du kan vurdere å installere en "Python versjonsforvalter" som [pyenv](https://github.com/pyenv/pyenv).

Du kan lese mer om oppsett og bruk her: https://github.com/pyenv/pyenv?tab=readme-ov-file#installation


