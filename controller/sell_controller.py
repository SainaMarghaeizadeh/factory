from controller.device_controller import DeviceController
from controller.costumer_controller import CostumerController
from model.da.sell_da import SellDa
from model.da.user_da import UserDa
from model.entity.sell import Sell
from model.entity.user import User


class SellController:
    @classmethod
    def save(cls, costumer_code, device_code, price, count, date):
        sell = Sell(
            costumer_code,
            device_code,
            price,
            count,
            date)
        print(sell)

        print("Controller - save: ",sell)
        sell_da = SellDa()
        sell_da.save(sell)

    @classmethod
    def edit(cls, costumer_code,device_code,price,count,date):
        sell = Sell(CostumerController.find_by_code(costumer_code),
            DeviceController.find_by_code(device_code),
            price,
            count,
            date)
        print("Controller - edit: ", sell)
        sell_da = SellDa()
        sell_da.edit(sell)


    @classmethod
    def remove(cls, code):
        sell_da = SellDa()
        sell_da.remove(code)
    @classmethod
    def find_all(cls):
        sell_da = SellDa()
        return sell_da.find_all()

    @classmethod
    def find_by_code(cls,code):
        sell_da = SellDa()
        print(sell_da.find_by_code(code))

    @classmethod
    def find_by_device_code(cls,device_code):
        sell_da = SellDa()
        print(sell_da.find_by_device_code(device_code)) \

    @classmethod
    def find_by_costumer_code(cls,costumer_code):
        sell_da = SellDa()
        print(sell_da.find_by_costumer_code(costumer_code))


