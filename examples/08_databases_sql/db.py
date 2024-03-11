import sqlite3
con = sqlite3.connect("db.sqlite")
cursor = con.cursor()
sensor = 1
query = f"""
SELECT ts, value 
FROM measurements 
WHERE sensor = {sensor}
order by ts desc
limit 10;
"""
cursor.execute(query)
all = cursor.fetchall()

for row in all:
    print(row)


cursor.close()
con.close()