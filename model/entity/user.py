class User:
    def __init__(self, user_name, password, costumer_code, active=True, code=0):
        self.code = code
        self.costumer_code = costumer_code
        self.user_name = user_name
        self.password = password
        self.active = active

    def __repr__(self):
        return str(self.__dict__)
