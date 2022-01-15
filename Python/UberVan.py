from car import Car

class UberVan(car):
    typeCarAccepted: list
    seatsMaterial: list

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super.__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial