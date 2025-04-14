# Activity One
# Base class: Superhero
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin
        self.__energy = 100  # private attribute

    def use_power(self):
        if self.__energy >= 10:
            self.__energy -= 10
            print(f"{self.name} uses {self.power}! Energy left: {self.__energy}")
        else:
            print(f"{self.name} is too tired to use {self.power}.")

    def rest(self):
        self.__energy = 100
        print(f"{self.name} has rested and is back to full energy!")

    def get_energy(self):
        return self.__energy  # getter for private energy

    def describe(self):
        print(f"{self.name} is a superhero from {self.origin} with the power of {self.power}.")

# Derived class: Speedster
class Speedster(Superhero):
    def __init__(self, name, origin, max_speed):
        super().__init__(name, "super speed", origin)
        self.max_speed = max_speed  # unique attribute for Speedsters

    def use_power(self):
        if self.get_energy() >= 15:
            # override method with Speedster-specific behavior
            self._Superhero__energy -= 15
            print(f"{self.name} dashes at {self.max_speed} mph! Energy left: {self.get_energy()}")
        else:
            print(f"{self.name} is too exhausted to run fast.")

# Create objects
hero1 = Superhero("Photon Blaze", "light manipulation", "Nova City")
hero2 = Speedster("Velocity Vibe", "Hyperion", 1200)

# Use methods
hero1.describe()
hero1.use_power()
hero1.rest()

print()

hero2.describe()
hero2.use_power()
hero2.use_power()
hero2.rest()

# Activity two
# Base class: Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement the move method.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print(f"{self.name}: Driving on the road! 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print(f"{self.name}: Flying in the sky! ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print(f"{self.name}: Sailing across the water! 🚢")

# Subclass: Train
class Train(Vehicle):
    def move(self):
        print(f"{self.name}: Rolling on the tracks! 🚆")

# Create instances
vehicles = [
    Car("Mustang"),
    Plane("Boeing 747"),
    Boat("Sea Explorer"),
    Train("Bullet Express")
]

# Loop through and call move()
for v in vehicles:
    v.move()
