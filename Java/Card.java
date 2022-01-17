public class Card extends Payment{
    
    String cardType;
    Integer expirationDate;
    String cvv;

    public Card(Integer id, String cardType, Integer expirationDate, String cvv) {
        super(id);

        this.cardType = cardType;
        this.expirationDate = expirationDate;
        this.cvv = cvv;

        this.printDataPayment();
    }

}