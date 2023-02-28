from sqlite3 import Connection

class Employee:
    __slots__ = ["_name", "_address", "_salary", "id"]
    connection = None
    cursor = None

    def __init__(self, name: str, address: str, salary: float):
        self._name = name
        self._address = address
        self._salary = salary
        self.id = None

    def get_name(self) -> str:
        return self._name

    def get_address(self) -> str:
        return self._address

    def get_salary(self) -> float:
        return self._salary

    def set_name(self, name: str):
        self._name = name

    def set_address(self, address: str):
        self._address = address

    def set_salary(self, salary: float):
        cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (str(salary), str(self.id)))
        Employee.connection.commit()
        print("Salary was changed")
        self._salary = salary

    name = property(fset=set_name, fget=get_name)
    address = property(fset=set_address, fget=get_address)
    salary = property(fset=set_salary, fget=get_salary)

    def __repr__(self):
        return f"Name: {self.name} Address: {self.address} Salary: {self.salary}"


def find_employee(id: int) -> Employee:
    Employee.cursor.execute("SELECT name, address, salary FROM employees WHERE id = ?", str(id))
    result = Employee.cursor.fetchone()
    if result:
        e = Employee(name=result[0], address=result[1], salary=result[2])
        e.id = id
        return e
    else:
        return None

# Factory Method
def create_employee(name: str, address: str, salary: float) -> Employee:
    # Lage ny objekt
    e = Employee(name, address, salary)
    # Finn ut hva som blir neste id
    Employee.cursor.execute("SELECT MAX(id) FROM employees")
    result = Employee.cursor.fetchone()
    next_id = result[0] + 1
    Employee.cursor.execute("INSERT INTO employees (id, name, address, salary) VALUES (?,?,?,?)", (str(next_id), name, address, str(salary)))
    e.id = next_id
    Employee.connection.commit()
    return e


# Main metode

conn = Connection("employees.sqlite")
cursor = conn.cursor()
Employee.cursor = cursor
Employee.connection = conn


# Lage ny medarbeider objekt
e = create_employee("Claire", "i Skogen",550000 )
print(e)

# Lønnsauke
#e.salary = 580000.01
#print(e)


