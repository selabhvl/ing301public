class Employee:
    __slots__ = ["_name", "_address", "_salary"]

    def __init__(self, name: str, address: str, salary: float):
        self._name = name
        self._address = address
        self._salary = salary

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
        self._salary = salary

    name = property(fset=set_name, fget=get_name)
    address = property(fset=set_address, fget=get_address)
    salary = property(fset=set_salary, fget=get_salary)

    def __repr__(self):
        return f"Name: {self.name} Address: {self.address} Salary: {self.salary}"


# Lage ny medarbeider objekt
e = Employee(name="Claire", address="i Skogen 3", salary=550000)
print(e)

# Lønnsauke
e.salary = 580000.01
print(e)


