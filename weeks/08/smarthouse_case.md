## Case Description: Smarthouse

Dere skal lage et programvaresystem for styring av et "smarthus"
Systemet kan installeres i forskjellige _bygninger_ (_Buildings_).
En byggning består av forskjellige _etasjer_ (_Floors_).
En etasje består av flere _rom_ (_Room_).
Et _rom_ har et _navn_ (f.eks. "stue", "kjøkken", "bad", ...) og hvert rom har et _areal_ målt i $m^2$.
Etasjer har et _etasjenummer_. Arealet til en etasje kan beregnes ved å summere arealene til de enkelte rommene.

Desto videre forvalter systemet _enheter_ (_devices_).
En enhet registreres med et _identifikasjonummer_ og dens produktegenskaper, dvs. _produsentnavn_, _modellnavn_ og hva for en enhet det dreier seg om (varmeovn, lyspære, strømmåler, osv.).
I tillegg kan enheten gis et _huskenavn_ (f.eks. "Varmepumpe Bad"). 
En enhet må registreres i ett rom i huset.

Vi skiller mellom to type enheter: _sensorer_ og _aktuatorer_. 

Eksempler på sensorer er temperturmålere, luftfuktighetsmålere, strømforbruksmålere, CO2 målere, bevegelsessensorer osv.
En sensor må ha en funksjon som leverer den siste _måleverdien_ og historien av tidligere måleverdiene.
En måleverdi består av _dato_, _klokkeslett_, _verdi_ (numerisk) og _måleenhet_ (f.eks. `°C` for temperatur, `%` for luftfuktighet osv.).

Aktuatorer er enheter som påvirker de fysiske omgivelsene.
Eksempler er panelovner, varmepumper, luftavfuktere, stikkkontakter, lyspærer osv. 
Aktuatorer har en _tilstand_ og funksjoner til å forandre denne interne tilstanden.
Noen aktuatorer kan bare slås av og på (f.eks. stikkontakt eller lyspære uten dimmer) mens andre kan styres i større grad (f.eks. kan varmepumpen settes til et ønsket temperatur som `21.3 °C`).

Til syvende og sist må det nevnes at noen enheter både viser sensor og aktutor egenskaper (f.eks en styrbart stikkontakt som samtidig måler strømmen) eller at noen sensorer måler forskjellige verdier samtidig (f.eks. en _luftkvalitetssensor_ måler CO2, luftfuktighet og VOC (flyktige organiske forbindelser) samtidig).