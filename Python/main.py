from car import Car
from account import Account

def run():
    car = Car("AMS234", Account("Andres Herrera", "M3ALD1"))
    car.id = 1
    print(vars(car))
    print(vars(car.driver))


if __name__ == "__main__":
    run()