from Prac_08.taxi import Taxi


class Silver_Service_Taxi(Taxi):
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flag fall of ${:.2f}".format(super().__str__(),
                                                     self.flag_fall)

    def get_fare(self):
        """Get the current fare."""
        return self.flag_fall + super().get_fare()
