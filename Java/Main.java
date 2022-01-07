class Main {
    public static void main(String[] args) {
        System.out.println("Hello world");
        Car car = new Car();
        car.license = "AMQ123";
        car.driver = "Andres Herrera";
        car.passenger = 4;
        car.printDataCar();

        Car car2 = new Car();
        car.license = "MAQJ21";
        car.driver = "Miguel Ocanto";
        car.passenger = 3;
        car.printDataCar();
    }
}