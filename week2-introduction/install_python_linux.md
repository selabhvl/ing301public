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
som vil gi deg informasjon hvilken Subversion av Python 3 du bruker.
Hvis kommandoen ovenfor skulle feile, så kan du etterinstallere Python med
```bash
sudo apt-get install python3 
```

## VS Code

Visual Studio Code kan installeres på Ubuntu gjennom en `.deb` Paket.
Du finner den på [denne siden](https://code.visualstudio.com/Download)

## PyCharm

PyCharm kan installeres gjennom _Snap_:

```bash
sudo snap install [pycharm-professional|pycharm-community] --classic
```
