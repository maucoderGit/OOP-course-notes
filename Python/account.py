class Account:
    id : int
    name: str
    document: str
    email: str
    __password: str

    def __init__(self, name: str, document: str):
        self.name = name
        self.document = document