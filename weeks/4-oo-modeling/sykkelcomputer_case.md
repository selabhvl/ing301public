# Case Description: Sykkelcomputer

En avansert sykkelcomputer består typisk av en eller flere ulike sensorer, 
eksempelvis en _GPS sensor_ som periodisk registrer posisjon i form av lengde- og breddegrad samt tidspunkt og høyde. 
En annen typisk sensor er en _fartsmåler_ (speedometer) som kontinuerlig viser den relative farten på sykkelen i forhold til underlaget.
Detsto videre kunne man tenke at en avansert sykkelcomputer har en _temperatur sensor_ som hele tiden måler aktuell temperatur og 
en koblingsmuligheter mot pulsklokke slik at den også vise aktuell _hjertefrekvens_ til syklisten.

En sykkelcomputer med GPS sensor har i tillegg en logging funksjonalitet som gjør det mulig å lagre en rute bestående av et antall GPS punkter. 
En rute kan lastes opp på datamskinen eller forskjellige cloud tjenester og viser statistikker bestående av
- Total lengde
- Total antall høydemeter (bare opp / opp og ned)
- Gjenommsnittlig hastighet
- Maks fart
- brukte Kalorier
- ...
Ruter kan til slutt sammenlignes med hverandre slik at sykkelcomputeren kan vise lengste rittet så langt, rute med høyest gjennomsnittsfart osv.
 
Sykkelcomputeren har et display som tilbyr interaksjon mot brukeren.
Display viser aktuell hastighet, gjennomsnittshastighet, totalt antall kjørte kilometer samt antall kilometer som er kjørt på den aktuelle ruten. 
Typisk finnes det knapper for å resette sensor data, starte en ny tur, lese ut GPS rute data, kalibrere høydemåler og også gjøre andre innstillinger.
 
På forelesningen skal vi se på hvordan vi kan identifisere klasser og relasjoner mellom klasser som kan danne utgangspunkt for Python kode som kan brukes til å representere problemområdet ovenfor. Vi skal bla.
 
- Identifisere klasser og relasjoner mellom klasser
- Se hvordan klasser og relasjoner kan representeres i et UML klasse diagram
- Finne ut hvilke metoder og instansvariable klassene skal ha
- Undersøke hvordan arv kan brukes ifm. modellering av problemstillingen
- Begynne å realisere klassene i Python kode

## Utvidelse Uke 5

Vi antar nå at det har kommet inn noen nye/ mer spesifikke krav angående sykkecomputeren.
Når en rute blir avsluttet skal den automatisk lagrest i en skyløsning (i første runden går vi utpå at vi barer lagrer den som en fil på disk).
Ved oppstart av sykkelcomputeren skal den prøver å kobler seg på skyløsningen (dvs. leser filene på disk) og synkroniserer sine rutetdata slik at informasjon over alle tidligere ruter er tilgjengelig.
I tillegg skal det være mmulig å lage rutegrupper.
En rutegruppe har et navn og kan inneholde et valgfri antall ruter eller undergrupper.
På en gruppe kan det føre samme type statistikk (total lenge, gjennomsnittsfart, ...) som på en rute.
