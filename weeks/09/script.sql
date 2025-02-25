SELECT sensor, value  -- velg kolonner
FROM measurements -- velg kildetabell
WHERE sensor = 2 -- velg rader: filtrering
ORDER BY value desc -- velg sortering
LIMIT 3; -- ta N første rader


SELECT *
FROM routes, sensors -- kryssprodukt av rader
WHERE route_no = id;

SELECT * FROM routes;

SELECT * FROM sensors;


-- spørring fra forskjellige tabeller
SELECT *
FROM measurements , sensors
WHERE sensor = id
AND sensor_type = 'speed'
ORDER BY value;


