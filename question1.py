class Superhero:
    
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self._secret_identity = secret_identity  # Protected attribute
        self.__power_level = power_level  # Private attribute
    
    @property
    def power_level(self):
        return self.__power_level
    
    @power_level.setter
    def power_level(self, value):
        if 0 <= value <= 100:
            self.__power_level = value
        else:
            raise ValueError("Power level must be between 0 and 100")
    
    def introduce(self):
        print(f"I am {self.name}! Power level: {self.__power_level}")
    
    def _reveal_secret(self):
        print(f"My secret identity is {self._secret_identity}")
    
    def use_power(self):
        raise NotImplementedError("Subclasses must implement this method")


class FlyingHero(Superhero):
   
    def __init__(self, name, secret_identity, power_level, max_altitude):
        super().__init__(name, secret_identity, power_level)
        self.max_altitude = max_altitude
    
    def use_power(self):
        print(f"{self.name} soars through the air at {self.max_altitude} feet!")
    
    def move(self):
        print("Flying high in the sky! ✈️")


class StrengthHero(Superhero):
    
    def __init__(self, name, secret_identity, power_level, lift_capacity):
        super().__init__(name, secret_identity, power_level)
        self.lift_capacity = lift_capacity
    
    def use_power(self):
        print(f"{self.name} lifts {self.lift_capacity} tons with ease!")
    
    def move(self):
        print("Running with super speed! 🏃‍♂️")



superman = FlyingHero("Superman", "Clark Kent", 95, 50000)
hulk = StrengthHero("Hulk", "Bruce Banner", 90, 100)

superman.introduce() 
superman.use_power() 
hulk.use_power()      

# Demonstrating encapsulation
try:
    superman.power_level = 150  # Will raise ValueError
except ValueError as e:
    print(f"Error: {e}")
