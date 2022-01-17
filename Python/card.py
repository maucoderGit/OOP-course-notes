from payment import Payment

class Card(Payment):
    card_type : str
    expiration_date: int
    cvv: str
    
    def __init__(self, id, card_type, expiration_date, cvv):
        super().__init__(id)
        self.card_type = card_type
        self.expiration_date = expiration_date
        self.cvv = cvv