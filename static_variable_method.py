STATIC VARIABLE
class Student:

    school = "ABC School"     

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)
        print("School:", Student.school)

s1 = Student("Sneha")
s2 = Student("Rahul")

s1.show()
print()
s2.show()
STATIC METHOD
class Math:

    @staticmethod
    def add(a, b):
        print("Sum =", a + b)

Math.add(20, 30)
