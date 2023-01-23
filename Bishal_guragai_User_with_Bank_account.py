from BankAccount import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        self.account.display_account_info()
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        self.display_user_balance()
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")

    # def transfer_money(self,amount,other_user):
    #     self.account.balance -=amount
    #     other_user.account.balance+=amount
    #     self.display_user_balance()
    #     other_user.display_user_balance
    #     return self
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self


robert = User("robert","robert@gmail.com")
silo = User("silo","silo@dogmail.com")
kenobi = User("Kenobi","kenobi@dogmail.com")

User.make_deposit(robert,100)
User.make_deposit(silo,100)
User.transfer_money(robert,silo,50)
user

