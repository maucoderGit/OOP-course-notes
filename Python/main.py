from car import Car
from account import Account
from UberX import UberX

def run():
    uber:dict = UberX("KASTH1", "Mauricio Gonzalez", "Tesla", "X")
    UberX.id=1

    print(vars(uber))

if __name__ == "__main__":
    run()