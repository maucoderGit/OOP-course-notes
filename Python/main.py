from payment import Payment
from paypal import Paypal
from car import Car
from account import Account
from UberX import UberX


def run():
    uber : object = UberX("KASTH1", "Mauricio Gonzalez", "Tesla", "X")
    UberX.id=1
    payment: object = Paypal("00e131k1", "Marketplace", "marketplace")
    payment.id = 1

    print(vars(uber))
    print(vars(payment))


if __name__ == "__main__":
    run()