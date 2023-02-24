# Uke 8: Structured Query Language

Denne uken har vi set på hvordan man "snakker" med en relasjonell database ved bruk av SQL.
Detter er deklarativt språk, dvs. vi må ikke bry oss om den interne fysiske
strukturen av vår data på disk. Istendenfor formulerer vi bare på et abstrakt 
nivå hva data vi vil ha fra databasen og hvordan den eventuelt skal forandres.

SQL kan grupperes inn i
- Spørringer som bare leser (Query Language)
  - `SELECT`
- Oppdateringer av tabellinnholdet (Data Manipulation Language)
  - `INSERT`
  - `UPDATE`
  - `DELETE`
- Oppdateringer på selve tabellstrukturen/skjema (Data Definition Language)
  - `CREATE`
  - `ALTER`
  - `DROP`

## SELECT

Den mest komplekse SQL uttrykket er med sikkert `SELECT` siden den 
gir nesten ubegrensete myuligheter i hvordan du kan hente ut data i tablleform.

Den grunnnlegennde strukturen ser slikt ut:
```sql
SELECT  -- Velger ut kolonnene eller anveder funksjoner på dem
    firstnamme,
    lastname,
    ects
FROM  -- Kildetabellen der data skal hentes fra
    students
WHERE  -- Betingelser / Filterkriterier som radene må oppfylle
    semester = 6
```

SQL kodeeksemplene fra forelesningen finner du [her](../../examples/08_databases_sql/lecture.sql)