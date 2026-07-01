MULTILEVEL INHERITANCE
class Person:
    def show_person(self):
        print("I am a Person.")

class Employee(Person):
    def show_employee(self):
        print("I am an Employee.")

class Manager(Employee):
    def show_manager(self):
        print("I am a Manager.")
MULTIPLE INHERITANCE
class Father:
    def father_quality(self):
        print("Father is hardworking.")

class Mother:
    def mother_quality(self):
        print("Mother is caring.")

class Child(Father, Mother):
    def child_quality(self):
        print("Child is talented.")

c = Child()

c.father_quality()
c.mother_quality()
c.child_quality()
