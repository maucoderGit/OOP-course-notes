class main {
    public static void main(String[] args) {
        // UberX uberX = new UberX("AMQ123",new Account("Andres Herrera", "A2W1233"), "Chevrolet", "Sonic");
        // uberX.setPassenger(4);
        // uberX.printDataCar();
        
        UberVan uberVan = new UberVan("LQK7K2", new Account("Mauricio Gonzalez", "K-109121"));
        uberVan.setPassenger(6);
        uberVan.printDataCar();
    }
}