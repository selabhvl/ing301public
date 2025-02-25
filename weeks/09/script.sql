SELECT sensor, value 
FROM measurements
WHERE sensor = 2
ORDER BY value desc
LIMIT 3;