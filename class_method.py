class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

print("Before:", Student.school)

Student.change_school("XYZ School")

print("After:", Student.school)
