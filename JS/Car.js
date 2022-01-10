class Car {
    constructor(license, driver){
        this.license = license;
        this.driver = driver;
        this.id;
        this.passenger;
    }
    printDataCar = () =>  {
        console.table(this.driver)
    }
}