#1
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_features(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
class Car(Vehicle):
    def __init__(self, make, model, year, doors, trunk_capacity):
        super().__init__(make, model, year)
        self.doors = doors
        self.trunk_capacity = trunk_capacity
    def display_features(self):
        super().display_features()
        print(f"Doors: {self.doors}, Trunk Capacity: {self.trunk_capacity} liters")
class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity, axles):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
        self.axles = axles
    def display_features(self):
        super().display_features()
        print(f"Cargo Capacity: {self.cargo_capacity} tons, Axles: {self.axles}")
class PickupTruck(Car, Truck):
    def __init__(self, make, model, year, doors, trunk_capacity, cargo_capacity, axles):
        Car.__init__(self, make, model, year, doors, trunk_capacity)
        Truck.__init__(self, make, model, year, cargo_capacity, axles)
    def display_features(self):
        print("Pickup Truck Features:")
        Vehicle.display_features(self)
        print(f"Doors: {self.doors}, Trunk Capacity: {self.trunk_capacity} liters")
        print(f"Cargo Capacity: {self.cargo_capacity} tons, Axles: {self.axles}")
pickup = PickupTruck("Ford", "Ranger", 2023, 4, 500, 2, 2)
pickup.display_features()

#2
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    def display_info(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}")
class Electronics(Product):
    def __init__(self, product_id, name, price, warranty_period, brand):
        super().__init__(product_id, name, price)
        self.warranty_period = warranty_period
        self.brand = brand
    def display_info(self):
        super().display_info()
        print(f"Warranty Period: {self.warranty_period} years, Brand: {self.brand}")
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material
    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}, Material: {self.material}")
laptop = Electronics("E101", "Laptop", 1200.50, 2, "Dell")
laptop.display_info()
print("\n")  # Line break for clarity
shirt = Clothing("C202", "Shirt", 35.75, "L", "Cotton")
shirt.display_info()
