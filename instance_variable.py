class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

car1 = Car("Toyota", 1200000)
car2 = Car("Hyundai", 900000)

car1.show()
print()

car2.show()
