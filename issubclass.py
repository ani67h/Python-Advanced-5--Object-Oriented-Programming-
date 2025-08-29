# defining parent class
class Vehicles:

    # constructor
    def __init__(vehicletype):
        print("Vehicle is a ",vehicletype)

# defining child class
class Car(Vehicles):

    # constructor
    def __init__(self):
        Vehicles.__init__("Car")

# driver's code
print(issubclass(Car, Vehicles)) 
print(issubclass(Vehicles, Car))       