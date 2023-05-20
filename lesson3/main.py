from car import Car
from human import Human

vlad = Human("Vlad", 1)
mikita = Human("Mikita", 1)
illia = Human("Illia", 1)
andrii = Human("Andrii", 0)
bronislav = Human("Bronislav", 0)

humans = list()
humans.append(vlad)
humans.append(mikita)
humans.append(illia)
humans.append(andrii)
humans.append(bronislav)
car = Car("BMW x6")
for human in humans:
    car.AddPassenger(human)
    car.AddDriver(human)

for passenger in car.Passengers:
    car.ToStringPassenger(passenger)
for driver in car.Drivers:
    car.ToStringDriver(driver)