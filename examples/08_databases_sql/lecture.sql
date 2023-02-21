SELECT start_ts -- projeksjon: utvlagte kolonner
FROM routes r  -- kildetabelll
WHERE route_no = 1 
OR route_no = 3  ;  -- predikat: filter

SELECT * FROM measurements m WHERE m.ts <> '2017-09-08T13:49:50.000';  


SELECT * FROM measurements, sensors  WHERE measurements.sensor = sensors.id ;

SELECT * FROM measurements FULL JOIN sensors ON measurements.sensor = sensors.id WHERE sensors.id = 4;

INSERT INTO sensors (id, sensor_type) VALUES (4, 'heart frequency');

SELECT * FROM sensors s ;

SELECT DATE(ts) AS dato, MAX(value) AS fart -- projeksjoner: utvalg av kolonner + funksjon
FROM measurements m  -- kildetabell
INNER JOIN sensors s ON s.id = m.sensor -- koblingstabell 
WHERE s.sensor_type = 'speed' -- predikat: filter
GROUP BY dato; -- gruppedanning for aggregasjon


UPDATE sensors -- tabellnavn
SET
 sensor_type = 'heartfq'
WHERE
 id = 4;


DELETE FROM sensors WHERE id = 4;


CREATE TABLE route_group (
	id INT NOT NULL,
	name TEXT NULL,
	speed_statistic REAL NULL
);

SELECT * FROM route_group rg ;


SELECT * FROM sqlite_schema ;

SELECT * FROM sensors s ;





