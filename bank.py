class Bank:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return f'{self.email} {self.password}'


class User(Bank):
    def __init__(self, email, password):
        super().__init__(email, password)


class Admin(Bank):
    def __init__(self, email, password):
        super().__init__(email, password)


user_1 = User('maminul2018@gmail.com', 2034059)
admin_1 = Admin('admin@gmail.com', 1234)
print(user_1)
print(admin_1)
