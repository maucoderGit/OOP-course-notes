class Car {
    Integer id;
    String license;
    Account driver;
    private Integer passenger;

    public Car(String license, Account driver){
        this.license = license;
        this.driver = driver;
        System.out.println("Passenger: " + passenger);
    }

    void printDataCar(){
        System.out.println("License: " + license + ", Name Driver: " + driver.name);
    }
}
