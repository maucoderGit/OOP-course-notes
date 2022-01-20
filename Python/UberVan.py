from car import Car

class UberVan(Car):
    """Class UberVan instance, herency"""
    typeCarAccepted: list
    seatsMaterial: list

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial

    # Override method setPassenger of super class Car for apply Polyomorphs
    def set_passenger(self, passenger):
        if passenger == 6:
            self.set_passenger = passenger
        else: 
            print("Minimal passenger acepted are 6.")