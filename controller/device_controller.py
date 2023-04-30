from controller.utils.validator import Validator
from model.da.device_da import DeviceDa
from model.entity.device import Device


class DeviceController:
    @classmethod
    def save(cls, name, model, count,avaiable=True):
        try:
            if Validator.persian_text(name) and \
                    Validator.persian_text(model) and \
                    Validator.zero_positive(count):
                device = Device(name, model, count, avaiable )
                device_da = DeviceDa()
                return True, device_da.save(device)
            else:
                print('error')
                raise ValueError("مقدارهای نامعتبر وارد شده است")
        except Exception as e:
            print(e.args)
            print(type(name))
            return False, f"Error : {e.args}"

    @classmethod
    def edit(cls, code, name, model, count, available):
        try:
            device = Device(name, model, count, available, code)
            device_da = DeviceDa()
            return True, device_da.edit(device)
        except Exception as e:
            return False, "Error :", e.args[1]

    @classmethod
    def remove(cls, code):
        try:
            device_da = DeviceDa()
            return True, device_da.remove(code)
        except Exception as e:
            return False, "Error :", e.args[1]

    @classmethod
    def find_all(cls):
        device_da = DeviceDa()
        return device_da.find_all()

    @classmethod
    def find_by_code(cls, code):
        device_da = DeviceDa()
        device = device_da.find_by_code(code)
        if device:
            device = device[0]
            device = Device(device[1],device[2],device[3],device[4],device[0])
            return device


    @classmethod
    def find_by_name(cls, name):
        device_da = DeviceDa()
        device = device_da.find_by_name(name)
        if device:
            print(device)
        else:
            return None

    @classmethod
    def find_available(self, available):
        device_da = DeviceDa()
        return device_da.find_available(available)

    @classmethod
    def find_exist(self, exists):
        device_da = DeviceDa()
        print(device_da.find_exist(exists))

    @classmethod
    def find_all_available(self):
        device_da = DeviceDa()
        return device_da.find_all_available()
