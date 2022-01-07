from car import Car

def run():
    car = Car()
    car.id = 1
    car.license = "AMS234"
    car.driver = "Andres Herrera"
    print(vars(car))

    car2 = Car()
    car2.id = 2
    car2.license = "MCE223"
    car2.driver = "Mauricio Gonzalez"
    print(vars(car2))


if __name__ == "__main__":
    run()