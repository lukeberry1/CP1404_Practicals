from Prac_08.taxi import Taxi


def Main():
    my_taxi = Taxi("Pruis 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    print(my_taxi.get_fare)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(my_taxi.get_fare)

Main()


