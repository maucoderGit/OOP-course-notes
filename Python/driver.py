from account import Account

class Driver(Account):

    def __init__(self, name: str, document: str):
        super().__init__(name, document)