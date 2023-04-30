from model.da.utils.da import DataAccess


class DeviceDa(DataAccess):
    def __init__(self):
        self.set_connection_string("localhost", "root", "saina13831383", "project_mft")

    def save(self, device):
        self.transaction("INSERT INTO device_tbl ("
                         "device_name,"
                         "device_model,"
                         "device_count,"
                         "device_available) VALUES (%s,%s,%s,%s)",
                         [device.name, device.model, device.count, device.available])
        return device

    def edit(self, device):
        self.transaction("UPDATE device_tbl SET "
                         "device_name=%s,"
                         "device_model=%s,"
                         "device_count=%s,"
                         "device_available=%s "
                         "WHERE code=%s",
                         [device.name, device.model, device.count, device.available, device.code])
        return device

    def remove(self, code):
        self.transaction("DELETE FROM device_tbl WHERE code=%s", [code])
        return code

    def find_all(self):
        return self.find("SELECT * FROM device_tbl")

    def find_by_code(self, code):
        return self.find("SELECT * FROM device_tbl WHERE code=%s", [code])

    def find_by_name(self, name , available=True):
        if available:
            return self.find("SELECT * FROM device_tbl WHERE device_name LIKE %s and device_count>%s and device_available=%s", [name,0,True])
        else:
            return self.find("SELECT * FROM device_tbl WHERE device_name LIKE %s", [name])

    def find_available(self, available):
        if available == True:
            return self.find("SELECT * FROM device_tbl WHERE device_available=%s", [True])
        elif available == False:
            return self.find("SELECT * FROM device_tbl WHERE device_available=%s", [False])

    def find_exist(self, exists):
        if exists == True:
            return self.find("SELECT * FROM device_tbl WHERE device_count>%s", [0])
        elif exists == False:
            return self.find("SELECT * FROM device_tbl WHERE device_count=%s", [0])


    def find_all_available(self):
        return self.find("SELECT * FROM device_tbl WHERE device_count>%s and device_available >%s",[0,0])
