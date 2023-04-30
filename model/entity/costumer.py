class Costumer:
    def __init__(self, name, family, birth_date, active=True, code=0):
        self.code = code
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.active = active

    def __repr__(self):
        return str(self.__dict__)
