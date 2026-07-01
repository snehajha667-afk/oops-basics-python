class Animal:
    def sound(self):
        print("Animals make sounds.")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

a = Animal()
d = Dog()

a.sound()
d.sound()
