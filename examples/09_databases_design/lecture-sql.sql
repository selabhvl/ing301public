SELECT * FROM measurements m ;

SELECT * FROM sensors s ;

SELECT * FROM routes r ;

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

-- Slett en kolonne
ALTER TABLE sensors DROP COLUMN name;



CREATE TABLE sensors_new (
	id INT NOT NULL,
	sensor_type TEXT NULL,
	PRIMARY KEY (id) -- nytt: primærnøkkel
);

INSERT INTO sensors_new VALUES (1, 'distance');
INSERT INTO sensors_new VALUES (1, 'speed'); -- dette går ikke fordi den strider mot PK constraint

CREATE TABLE measurements_new(
	sensor_id INT NOT NULL,
	ts TEXT NOT NULL,
	value REAL NOT NULL,
	PRIMARY KEY (sensor_id, ts),
	FOREIGN KEY (sensor_id) REFERENCES sensors_new (id)
);

INSERT INTO measurements_new VALUES (2, '2021-01-01', 42);

SELECT * FROM measurements_new ;








