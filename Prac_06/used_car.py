"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    limo = Car(100)
    my_car.drive(30)
    limo.add_fuel(20)
    limo.drive(150)
    print("limo fuel =", limo.fuel)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print("limo odo =", limo.odometer)
    print(limo)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()