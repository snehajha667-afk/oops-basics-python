class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary    # Private variable

    def show(self):
        print("Name:", self.name)
        print("Salary:", self.__salary)

emp = Employee("Sneha", 50000)

emp.show()
