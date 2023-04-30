from model.da.user_da import UserDa
from model.entity.user import User

class UserController:
    @classmethod
    def save(cls,username,password,costumer_code,user_active=1):
        user = User(username,password,costumer_code,user_active)
        user_da = UserDa()
        user_da.save(user)
    @classmethod
    def edit(cls,username,password,costumer_code,active,code):
        user = User(username,password,costumer_code,active,code)
        user_da = UserDa()
        user_da.edit(user)
    @classmethod
    def remove(cls,code):
        user_da = UserDa()
        user_da.remove(code)


    @classmethod
    def find_all(cls):
        user_da = UserDa()
        print(user_da.find_all())

    @classmethod
    def find_by_code(cls,code):
        user_da = UserDa()
        print(user_da.find_by_code(code))

    @classmethod
    def is_valid_user(cls,user_name,password):
        user_da = UserDa()
        print(user_da.is_valid_user(user_name,password))