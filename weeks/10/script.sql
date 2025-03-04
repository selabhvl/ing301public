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
from measurements mm
inner join sensors ss on ss.id = mm.sensor 
where s.sensor_type = 'speed');

-- DML demonstrasjon
SELECT * from sensors s ;


UPDATE sensors SET sensor_type='fart';

DELETE from sensors;



-- DDL demonstratsjon

insert into users (id, email, score) values (1, 'past@hvl.no', null); -- null = None

CREATE table users (
	id integer not null, -- int
	email text not null, -- str
	score real null -- float
);

SELECT * from users;
