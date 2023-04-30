from model.da.utils.da import DataAccess


class UserDa(DataAccess):
    def __init__(self):
        self.set_connection_string("localhost", "root", "saina13831383", "project_mft")

    def save(self, user):
        self.transaction(
            "INSERT INTO user_tbl (user_username,user_password,user_costumer_code,user_active) VALUES (%s,%s,%s,%s)",
            [user.user_name, user.password, user.costumer_code, user.active])

    def edit(self, user):
        self.transaction(
            "UPDATE user_tbl SET user_username=%s, user_password=%s,user_costumer_code=%s, user_active=%s WHERE CODE=%s",
            [user.user_name, user.password, user.costumer_code,user.active, user.code])

    def remove(self, code):
        self.transaction("DELETE FROM user_tbl WHERE code=%s", [code])

    def find_all(self):
        return self.find("SELECT * FROM user_tbl")

    def find_by_code(self, code):
        return self.find("SELECT * FROM user_tbl WHERE code=%s", [code])

    def is_valid_user(self,user_name,password):
        return self.find("SELECT * FROM user_tbl WHERE user_username=%s and user_password=%s", [user_name,password])

