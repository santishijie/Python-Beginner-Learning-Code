class User():
    def __init__(self, first, last, *qita):
        self.first_name = first
        self.last_name = last
        self.qita = qita

    def describe_user(self):
        print(f"the users' first name is {self.first_name},last name is {self.last_name}")
        if self.qita:
            print("else:")
            for i in self.qita:
                print(i)

    def greet_user(self):
        print(f"{self.first_name} {self.last_name},Welcome")


class Admin(User):
    def __init__(self, first, last, privileges):
        super().__init__(first, last)
        self.privileges = privileges

    def show_privileges(self):
        # print(self.privileges)
        Privileges()


class Privileges():
    def __init__(self):
        self.privileges = 'SB'
        print('you are ' + self.privileges)


user01 = User('zhenhao', 'yuan', '22', 'postgraduate')
user02 = Admin('zhenhao', 'yuan', 'can add post')
user02.show_privileges()
