from account import Account

class Car:
    id: int
    license: str
    driver: object = Account(str, str)
    __passenger: int

    def __init__(self, license ,driver):
        self.license = license
        self.driver = driver
        self.__passenger: int

    def get_passenger(self):
        if self.__passenger != int:
            print(f'{self.__passenger}')

    def set_passenger(self, __passenger):
        if __passenger >= 4:
            self.__passenger = __passenger
            print(f'passengers asigned are: {self.__passenger}')

        else: 
            print(f'minimun passenger need are: {self.__passenger}')