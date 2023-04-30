from model.da.utils.da import DataAccess


class SellDa(DataAccess):
    def __init__(self):
        self.set_connection_string("localhost", "root", "saina13831383", "project_mft")

    def save(self, sell):
        print("Sell:", sell)
        self.transaction(
            "INSERT INTO sell_tbl (costumer_code,device_code,sell_price,sell_count,sell_date) VALUES (%s,%s,%s,%s, %s)",
            [sell.costumer_code, sell.device_code, sell.price, sell.count, sell.date])

    def edit(self, sell):
        self.transaction(
            "UPDATE sell_tbl SET costumer_code=%s, device_code=%s,sell_price=%s ,sell_count =%s, sell_date=%s WHERE code=%s",
            [sell.costumer_code, sell.device_code, sell.price, sell.count, sell.date, sell.code])

    def remove(self, code):
        self.transaction("DELETE FROM sell_tbl WHERE code=%s", [code])

    def find_all(self):
        query = "SELECT * FROM sell_tbl s INNER JOIN costumer_tbl c ON s.costumer_code = c.code INNER JOIN device_tbl d ON s.device_code = d.code;"
        return self.find(query)

    def find_by_code(self, code):
        return self.find("SELECT * FROM sell_tbl s  WHERE code=%s", [code])

    def find_by_costumer_code(self, costumer_code):
        return self.find("SELECT * FROM sell_tbl WHERE costumer_code=%s", [costumer_code])

    def find_by_device_code(self, device_code):
        return self.find("SELECT * FROM sell_tbl WHERE device_code=%s", [device_code])
