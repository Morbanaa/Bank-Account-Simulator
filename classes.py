class Bank():
    def __init__(self,balance):
        self.balance = balance

    def deposit(self):
        while True:
            try:
                amount = float(input("Enter amount to deposit: "))

                if amount <= 0:
                    print("The value must be greater than zero!")
                    continue
                else:
                    self.balance += amount

                break
            except ValueError:
                print("Value Error! Must be a number!")

    def withdraw(self):
        while True:
            try:
                amount = float(input("Enter amount to withdraw: "))

                if amount <= 0:
                    print("The value must be greater than zero!")
                    continue
                elif amount > self.balance:
                    print("Insuficent Funds!")
                    continue
                else:
                    self.balance -= amount

                break
            except ValueError:
                print("Value Error! Must be a number!")
        

    def check_balance(self):
        print(f"Balance: ${self.balance:.2f}")
        input("Hit enter to continue...")
