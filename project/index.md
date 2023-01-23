# Programmeringsprosjekt: Smart Home

Det obligatoriske prosjekt i ING301 er bygget rundt den samme case-studien: 
Å bygge en system som kan styre en "_Smart Home_", sammenlignbar med f.eks. [Home Assistant](https://www.home-assistant.io/).

![Smart Home Infografikk](../resources/images/smart-home.jpg)

## Intro

_Smarthus_ er et begrep som dekker forskjellige typer _hjemmeautomatisering_.
Dette er basert på "_intelligente_" enheter (_Internet of Things (IOT)_ devices) som kan kommuniserere gjennom forskjellige nettverksteknologier og dermed muliggjør bla. overvåkning, regulering og optimalisering.
For eksempel kan en internettstyrt temperatursensor og panelovn styres slik at de holder temperaturen i et rom på et viss nivå eller en intelligent strømmåler kan prøve å optimalisere strømforbruket.
Systemet dere skal utvikle skal først og fremst forvalte forskjellige typer enheter, dvs. lokasjonen, måleverdier eller tilstand (er enheten slått på eller av)

## Domenebeskrivelse

SmartHus systemet kan installeres i forskjellige _byggninger_ (_Buildings_).
En byggning består av forskjellige _etasjer_ (_Floors_) som selv består av flere _rom_ (_Room_).
Et _rom_ kan gis et _navn_ (f.eks. "stue", "kjøkken", "bad", ...) også har det et _areal_ målt i $m^2$.
Etasjer har et _etasjenummer_, arealet til en etasje kan beregnes ved å summere arealene til de enkelte rommene.
Desto videre forvalter systemet _enheter_ (_Device_).
En enhet registreres med et teknisk identifikasjonummer (vanligvis satt hos produsenten).
I tillegg kan enheten gis et _husknavn_ (f.eks. "Varmepumpe Bad") og produktegenskaper registreres, dvs. _produsentnavn_ og _modellnavn_. 
Enheten registreres alltid i ett rom.
Stort sett kan man skiller mellom to typer enheter: _sensorer_ og _aktuatorer_.
Sensorer måler forskjellige type verdier.
Eksempler er temperturmålere, luftfuktighetsmålere, strømforbruksmålere, CO2 målere, bevegelsessensorer osv.
En sensor kan spørres om det nåværende _måleverdi_ og historien av alle tidligere måleverdiene.
En måleverdi består av _dato_, _klokkeslett_, _verdi_ (numerisk) og _enhet_ (f.eks. `°C` for temperatur, `%` for luftfuktighet osv.).
Aktuatorer er enheter som påvirker de fysiske omgivelsene.
Eksempler er panelovener, varmepumper, luftavfuktere, stikkkontakter, lyspærer osv. 
Aktuatorer har en _tilstand_ og funksjoner til å forandre denne interne tilstanden.
Noen aktuatorer kan bare slås av og på (f.eks. stikkontakt eller lyspære uten dimmer) mens andre kan styres i større grad (f.eks. kan varmepumpen settes til `21.3 °C`).
Til syvende og sist må det nevnes at noen enheter viser sensor og aktutor egenskaper (f.eks en styrbart stikkontakt som samtidig måler strømmen) eller at sensorer måler måler forskjellige ting samtidig (
F.eks. en _luftkvalitetssensor_ måler CO2, luftfuktighet og VOC (flyktige organiske forbindelser) samtidig).


## Oppgaver

Mer informasjon om de fire deloppgavene i prosjektet blir lagt ut fortløpende i kursforløpet.

### Del A: Domenemodell og grunnlegende Funksjonaliteter

I første prosjektsteg skal du legge grunnlag for hele systemet ved å _planlegge_ og _implementere_ en _domenemodell_.

### Del B: Datalagring

I neste steg skal du sørger få at informasjon blir lagret permanent på en harddisk når systemet avsluttes og at denne lagrete informasjonen kan leses igjen.

### Del C: Nettbasert tilgang

I dette steget skal du bruke nettverksprotokoll for å koble systemet mot eneheter som tilbyr en slik grensesnitt også skal du øffentliggjøre enkelte funksjoner gjennom en web-grensesnitt.

### Del D: Integrasjon med andre enheter

I det siste steget skal du simulere integrasjon av forskjellige Hardware enheter.

