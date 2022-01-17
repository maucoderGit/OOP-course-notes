class Account:
    id : int
    name: str
    document: str
    email: str
    password: str

    def __init__(self, name, document, password, email):
        self.name = name
        self.email = email
        self.password = password
        self.document = document