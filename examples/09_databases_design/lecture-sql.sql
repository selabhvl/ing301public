SELECT * FROM measurements m ;

SELECT m.sensor, max(value), min(value), avg(value) FROM routes r -- kildetabell
INNER JOIN measurements m  -- kobler sammen med rutemålinger
ON DATETIME(r.start_ts) <= DATETIME(m.ts) -- der de ligger i intervall
AND DATETIME(m.ts) <= DATETIME(r.end_ts) 
WHERE r.route_no = 1 -- for rute med nummer 1
GROUP BY m.sensor 
HAVING min(value) >= 0;  -- filterkriterier for grupper


SELECT AVG(value) FROM measurements m  WHERE m.sensor = 3; -- Finding average speed

-- finn alle fartålinger som ligger over gjennomsnittet
SELECT * FROM measurements m WHERE m.sensor = 3
AND value > (SELECT AVG(value) FROM measurements m  WHERE m.sensor = 3); -- delspørring


-- Vekselvirkende delspørring: over gjennomsnitt i dens sensorkategori
SELECT * FROM measurements m1 WHERE 
 value > (SELECT AVG(value) FROM measurements m2  WHERE m1.sensor = m2.sensor); -- Vekselvirkende delspørring
 
 
SELECT * FROM sensors s ;

--Legg til en kolonne
ALTER TABLE sensors ADD COLUMN name TEXT;