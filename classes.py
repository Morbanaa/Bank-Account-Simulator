class Bank():
    def __init__(self,balance):
        self.balance = balance

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def check_balance(self):
        print(f"Balance: ${self.balance:.2f}")
        input("Hit enter to continue...")
