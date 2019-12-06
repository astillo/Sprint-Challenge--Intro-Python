# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle(object):
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

class GroundVehicle(Vehicle):
    pass
class Car(GroundVehicle):
    pass
class Motorcycle(Vehicle):
    pass

class FlightVehicle(Vehicle):
    def __init__(self, wings):
        self.wings = wings

class Airplane(FlightVehicle):
    pass

class Starship(Vehicle):
    def __init__(self, fuel):
        self.fuel = fuel

