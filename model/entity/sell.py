from controller.costumer_controller import CostumerController
from controller.device_controller import DeviceController


class Sell:
    def __init__(self, costumer_code, device_code, price, count, date, code=0):
        self.code = code
        self.costumer_code = costumer_code
        self.device_code = device_code
        self.price = price
        self.count = count
        self.date = date

    def __str__(self):
        return str(self.__dict__)
