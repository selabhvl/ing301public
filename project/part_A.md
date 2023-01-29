# Part A: Domenemodell og Basisfunksjonalitet

## Utsjekk og 'kom i gang'

## Demo-Hus

For å teste din implementasjon på et eksempel skal et "demo hus" legges inn i systemet.
Dette skal gøres i funksjonen `build_demo_house()` i `main.py`.
Demo-huset er beskrivet [her](./demo.md).

## Implementasjonskrav

For å kunne sammligne deres løsninger må alle enheter viser en enhetlig _representasjon_ når disse skrives ut.
I Python kan man bruke `print()` funksjonen til å skrive ut en objekt.
Standardmessig er denne presentasjonen veldig generisk og gir bare informasjon over klasse og memory-adresse.
Man kan forandre denne oppførelsen ved å overskriver ``__repr__()`` funksjonen i en gitt klasse:
```python
class MyObject:
    
    def __repr__(self):
        return "my custom representation here"
```
I deres applikasjon skal enheter skrives ut i følgende format:
```
<Sensor eller Aktuator>(<serienummer) TYPE: <enhetstype> STATUS: <enhetsstatus> PRODUCT DETAILS: <produsent> <produktnavn>
```
I `enhentstype` finner man hva type enhet man ser på (Smart Lys, Temperatursensor, osv).
Alle relevante enhetstyper finner du i [beskrivelsen av demo-huset](./demo.md).
Hvis enheten er en sensor skal `enhetsstaus` viser den nåværende måleverdien med enhet (`°C` for Temperatur, `%` for Luftfuktighet, `kWh` for Strøm, `g/m^3` for Luftkvalitet).
Hvis enheten er en aktuator som styrer temperatur (altså panelovener, varmepumper og gulvvarme) så skal status viser temperaturen som ehenten er stilt inn på.
For øvrige aktuator vises bare om enheten er på (`ON`) eller av (`OFF`). 

Nedenfor noen eksempler:
```
Sensor(e237beec-2675-4cb0) TYPE: Temperatursensor STATUS: 3.2 °C PRODUCT DETAILS: Moen Inc Prodder Ute 1.2
Aktuator(f11bb4fc-ba74-49cd) TYPE: Smart Lys STATUS: OFF PRODUCT DETAILS: Fritsch Group Tresom Bright 1.0
Aktuator(eed2cba8-eb13-4023) TYPE: Varmepumpe STATUS: 16.0 °C PRODUCT DETAILS: Osinski Inc Fintone XCX2FF
```
