class Account:
    id : int
    name: str
    document: str
    email: str
    __password: str

    def __init__(self, name: str, document: str, password: str, email: str):
        self.name = name
        self.email = email
        self.password = password
        self.document = document