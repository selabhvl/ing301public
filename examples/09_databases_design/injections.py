from sqlite3 import Connection


conn = Connection("employees.sqlite")
cursor = conn.cursor()

print("Employee Database")
print("Please enter employee id: ",  end="")
id = input()
if id != "3":
    cursor.execute("SELECT name, address FROM employees WHERE id = " + id)
    print("Name\tAddress")
    rows = cursor.fetchall()
    for row in rows:
        print("\t".join(row))
else:
    print("You are not allowed to see this employee!")

conn.close()