from model.da.utils.da import DataAccess

class CostumerDa(DataAccess):
    def __init__(self):
        self.set_connection_string("localhost", "root", "saina13831383", "project_mft")

    def save(self, costumer):
        self.transaction(
            "INSERT INTO costumer_tbl (costumer_name,costumer_family,costumer_birth_date, costumer_active) VALUES (%s,%s,%s,%s)",
            [costumer.name, costumer.family, costumer.birth_date, costumer.active])

    def edit(self, costumer):
        self.transaction(
            "UPDATE costumer_tbl SET costumer_name=%s, costumer_family=%s, costumer_birth_date=%s, costumer_active=%s WHERE code=%s",
            [costumer.name, costumer.family, costumer.birth_date, costumer.active, costumer.code])

    def remove(self, code):
        self.transaction("DELETE FROM costumer_tbl WHERE code=%s", [code])

    def find_all(self):
        return self.find("SELECT * FROM costumer_tbl")

    def find_by_code(self, code):
        return self.find("SELECT * FROM costumer_tbl WHERE code=%s", [code])

    def find_by_name_family(self, name, family):
        return self.find("SELECT * FROM costumer_tbl WHERE name LIKE %s and family Like %s", [name + "%", family + "%"])
