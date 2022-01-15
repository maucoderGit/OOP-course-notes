import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car{

    Map<String, Map<String,Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;

    public UberVan(String license, Account driver, Map
        <String, Map<String,Integer>> typeCarAccepted, 
        ArrayList<String> seatsMaterial){
            super(license, driver);
            this.seatsMaterial = seatsMaterial;
            this.typeCarAccepted = typeCarAccepted;
    }
}