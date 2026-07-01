class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)

s = Student("Sneha", 101)

s.display()
