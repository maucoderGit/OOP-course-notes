from driver import Driver

class Car:
    id: int
    license: str
    driver: object = Driver(str, str)
    _passenger: int

    def __init__(self, license ,driver):
        self.license = license
        self.driver = driver

    def get_passenger(self):
        if self._passenger != int:
            print(f'{self._passenger}')

    def set_passenger(self, _passenger):
        if _passenger >= 4:
            self._passenger = _passenger
            print(f'passengers asigned are: {self._passenger}')

        else: 
            print(f'minimun passenger need are: {self._passenger}')