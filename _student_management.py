class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Roll :", self.roll)
        print("Marks:", self.marks)

student1 = Student("Sneha", 101, 90)
student2 = Student("Rahul", 102, 85)

student1.display()
student2.display()
