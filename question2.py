class Animal:    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Fish(Animal):
    def move(self)
        print("Swimming through water! 🐟")


class Bird(Animal):   
    def move(self):
        print("Flying through the air! 🦅")

class Snake(Animal):
    def move(self):
        print("Slithering on the ground! 🐍")

class Vehicle:
    def move(self):
      raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):   
    def move(self):
        print("Driving on the road! 🚗")


class Boat(Vehicle):
    def move(self):
        print("Sailing on water! ⛵")


class Airplane(Vehicle): 
    def move(self):
        print("Flying through the sky! ✈️")

def demonstrate_movement(entities):
    for entity in entities:
        entity.move()

animals = [Fish(), Bird(), Snake()]
vehicles = [Car(), Boat(), Airplane()]

print("Animal Movements:")
demonstrate_movement(animals)

print("\nVehicle Movements:")
demonstrate_movement(vehicles)
