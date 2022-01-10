class Main {
    public static void main(String[] args) {
        System.out.println("Hello world");
        Car car = new Car("AMQ123", new Account("Andres Herrera", "A2W1233"));
        car.printDataCar();

        Car car2 = new Car("MAQJ21", new Account("Miguel Ocanto", "NAQ3912"));
        car2.printDataCar();
    }
}