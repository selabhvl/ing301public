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

sElEcT

-- spørring fra forskjellige tabeller
SELECT value
FROM measurements 
inner JOIN sensors ON id = sensor 
where sensor_type = 'speed'
order by value desc
limit 1;


-- demo: aggregasjoner
SELECT 
sensor_type,
min(value), 
max(value),
avg(value),
count(distinct value)
FROM measurements 
inner JOIN sensors ON id = sensor
group by sensor_type;
--where sensor_type = 'speed';


SELECT 
route_no ,
route_no + 1
FROM routes;


SELECT timediff(end_ts , start_ts), route_no, 'hei' FROM routes;


INSERT INTO sensors (id, sensor_type ) values (4, 'heart_frequency');
insert into measurements (sensor, ts, value) values (5, '2017-08-13 08:52:26', 42);

