class Device:
    def __init__(self, name, model, count=1, available=True, code=0):
        self.code = code
        self.name = name
        self.model = model
        self.count = count
        self.available = available

    def __repr__(self):
        return str(self.__dict__)
