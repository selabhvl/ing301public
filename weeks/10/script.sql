-- oppsummering forrige uke
SELECT sensor_type, avg(value), max(value), min(value) 
FROM measurements  m
inner join sensors s on m.sensor = s.id
group by sensor_type;


-- Oppgave: Finner alle målingene som ligger over gjenommsnittet

SELECT avg(value)
from measurements m
inner join sensors s on s.id = m.sensor 
where s.sensor_type = 'speed';

SELECT count(*)
from measurements m
inner join sensors s on s.id = m.sensor 
where s.sensor_type = 'speed'
and m.value > 18.83;

-- delspørringer


SELECT count(*)
from measurements m
inner join sensors s on s.id = m.sensor 
where s.sensor_type = 'speed'
and m.value > (SELECT avg(value) -- skalar delspørring
from measurements m
inner join sensors s on s.id = m.sensor 
where s.sensor_type = 'speed');