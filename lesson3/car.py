from human import Human
class Car:
    def __init__(self, brand):
        self.Brand = brand
        self.Passengers = list()
        self.Drivers = list()
    def AddPassenger(self, human = Human()):
        if(human.Role == 0):
            self.Passengers.append(human.Name)
    def AddDriver(self, human = Human()):
        if(human.Role == 1):
            self.Drivers.append(human.Name)
    def ToStringPassenger(self, human = Human()):
        print(f"Passenger of {self.Brand} is {human.__str__()}")
    def ToStringDriver(self, human = Human()):
        print(f"Driver of {self.Brand} is {human.__str__()}")
