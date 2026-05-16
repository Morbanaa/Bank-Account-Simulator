import platform
import os
from classes import Bank

def main():
    bank = Bank(1000)
    while True:
        clear_screen()
        print("-------------------------------")
        print("               Bank")
        print("-------------------------------\n")

        print("Would you like to:")
        print("(A) Check Balance:")
        print("(B) Withdraw Funds:")
        print("(C) Deposit Funds:")
        print("(D) Exit Program:")
        choice = input("Choose: ").upper()

        match choice:
            case "A":
                bank.check_balance()
            case "B":
                bank.withdraw()
            case "C":
                bank.deposit()
            case "D":
                break
            case _:
                continue

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()

    clear_screen()
    print("\nHave a great day\n")
