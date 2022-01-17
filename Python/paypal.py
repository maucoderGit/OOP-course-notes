from payment import Payment

class Paypal(Payment):
    reference: str
    sucursal: str

    def __init__(self, id, reference, sucursal):
        super().__init__()
        self.reference = reference
        self.sucursal = sucursal