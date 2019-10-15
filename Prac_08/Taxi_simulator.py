from Prac_08.car import Car
from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import Silver_Service_Taxi

MENU = """a) Choose taxi
b) Drive
c) Quit"""


def main():
    taxis = [Taxi("Prius", 100), Silver_Service_Taxi("Limo", 100, 2),
             Silver_Service_Taxi("Hummer", 200, 4)]
    print(MENU)
    choice = input(">>>").upper()
    total_bill = 0
    choosen_taxi = None
    while choice != "C":
        if choice == "A":
            print("Taxis available:")
            taxi_list(taxis)
            taxi_choice = int(input("choose taxi:"))
            choosen_taxi = taxis[taxi_choice]
        elif choice == "B":
            drive_taxi(choosen_taxi, total_bill)
        print("Bill to date ${}".format(total_bill))
        print(MENU)
        choice = input(">>>").upper()


def taxi_list(taxis):
    for i, taxi in enumerate(taxis):
        print("{} {}".format(i, taxi))


def drive_taxi(choosen_taxi, total_bill):
    choosen_taxi.start_fare()
    distance_to_drive = int(input("How far are we driving:"))
    choosen_taxi.drive(distance_to_drive)
    fare = choosen_taxi.get_fare()
    total_bill += fare
    print("Your current taxi {} fare for this drive is ${}".format(choosen_taxi.name, fare))
    return total_bill



main()
