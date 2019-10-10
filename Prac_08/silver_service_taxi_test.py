from Prac_08.silver_service_taxi import Silver_Service_Taxi


def Main():
    Taxi = Silver_Service_Taxi("flash taxi", 20, 2)
    Taxi.drive(18)
    print(Taxi)
    print(Taxi.get_fare())

Main()