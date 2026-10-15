class bank:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("deposited:", amount)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdrawal:",amount)
        else:
            print("insufficient balance")
    def check_balance(self):
        print("balance:",self.balance)
b1 = bank(1000)
amount = float(input("enter deposit amount: "))
b1.deposit(amount)

amount = float(input("enter withdrawal amount: "))
b1.withdraw(amount)

b1.check_balance()

