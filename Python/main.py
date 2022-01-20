from payment import Payment
from paypal import Paypal
from car import Car
from account import Account
from UberX import UberX


def run():
    uber : object = UberX("KASTH1", "Mauricio Gonzalez", "Tesla", "X")
    uber.id = 1
    payment: object = Paypal("00e131k1", "Marketplace", "marketplace")
    payment.id = 1
    car: object = Car("LJWKK", ("Mauricio", "KIESA"))
    car.set_passenger(4)
    uber.set_passenger(4)

    print(vars(car))
    print(vars(uber))
    print(vars(payment))


if __name__ == "__main__":
    run()