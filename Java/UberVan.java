import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car{
    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    
    public UberVan(String license, Account driver){
        super(license, driver);
    }

    // public UberVan(String license, Account driver, 
    //     Map<String, Map<String,Integer>> typeCarAccepted,
    //     ArrayList<String> seatsMaterial){
    //         super(license, driver);
    //         this.seatsMaterial = seatsMaterial;
    //         this.typeCarAccepted = typeCarAccepted;
    //     }
    
    @Override
    public void setPassenger(Integer passenger){
        if (passenger >= 6){
            this.passenger = passenger;
        }else{
            extracted(passenger);
        }
    }

    private void extracted(Integer passenger) {
        System.out.println("Minimum passenger are 6 and you give " + passenger);
    }
}