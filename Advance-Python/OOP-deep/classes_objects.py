"""
Object-Oriented Programming (OOP) is not a magic. It's just a way to model the real world in code so our programs become:
    >> Resuable
    >> Organized
    >> Easy to maintain and extend
Thinking of OOP like a building with LEGO:
>> Class = The instruction booklet/mold
>> Object = The actual LEGO model we build
>> Attributes = The color and sizes of bricks
>> Methods = The actions we can do with the model (spin it, attach more bricks etc.)

Python's four main OOP pillers (the ones everyone talks about):
"""


class Car:  # This is the blueprint (class )
    # class variable (shared by all cars)
    wheels = 4

    def __init__(
        self, brand, model, year
    ):  # constructor - runs when we create an object
        self.brand = brand  # instance variables (unique to each car)
        self.model = model
        self.year = year
        self.odometer = 0  # default value

    def drive(self, km):  # method (action)
        self.odometer += km
        print(f"{self.brand} {self.model} drove {km}. Total: {self.odometer} km")

    def __str__(self):  # Special method - makes print (car) nice
        return f"{self.year} {self.brand} {self.model} ({self.odometer} km)"


# Creating objects (instances)
my_car = Car("Toyota", "Corolla", 2022)
frinds_car = Car("Tesla", "Model 3", 2024)

my_car.drive(150)
my_car.drive(10000)
print(my_car)
