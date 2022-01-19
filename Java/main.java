class main {
    public static void main(String[] args) {
        UberX uberX = new UberX("AMQ123",new Account("Andres Herrera", "A2W1233"), "Chevrolet", "Sonic");
        uberX.setPassenger(3);
        uberX.printDataCar();
    }
}