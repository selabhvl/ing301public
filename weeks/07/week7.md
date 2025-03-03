
# Uken 7: Tirsdag 11. februar 2025

Siste forelesning om _objektorientering_.
Hovedtema er _designmønstre_ (_design patterns_).
Den primære referansen om designmønstre er boken ["_Design Patterns: Elements of Reusable Object-Oriented Software_"](https://en.wikipedia.org/wiki/Design_Patterns).
I forelesningen fokuserer vi på:

- Kompositt (Composite),
- Iterator, og
- Strategi

I filen [`routes.py`](./routes.py) har vi laget en _linked list_ (som er en eksempel av kompositt mønstren) fra bunn av, laget en iterator for dem (slik at en kan bruke "`for .. in `" syntaks) og laget forskjellige aggregasjoner som strategier. 

## Andre tema:

I tillegg har vi også sett på hvordan [_klassevariabler_ fungerer](./klassevariabel.py) og hvordan man kan bruke `__slots__` og _properties_ for å lage _uforanderlig objekter og klasse_ (se [`coordinates.py`](./coordinates.py).

