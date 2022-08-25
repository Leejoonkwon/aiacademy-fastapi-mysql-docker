from app.models.user import User

class UserService(object):
    def __init__(self) -> None:
        pass
    def typing(self,ID,password):
        typing = User(ID,password)
        print(f'ID : abc')
        print(f'password :def')