""" Write a Python program to simulate an ATM system using multiple functions. The program should start by asking the user for their name and an initial balance. """


def display_main_menu():
    print("ATM Menu:\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    option = int(input("Please choose and option (1-4): "))
    return option
    
def deposit(balance):
    deposit = float(input("Enter the amount to deposit: "))
    balance += deposit
    print(f"Deposited: ${deposit}. New Balance: ${balance}")
    return balance
    

def withdraw(balance):
    withdraw = float(input("Enter an amount to withdraw: "))
    if balance <= 0 or balance < withdraw:
        print("Error cannot withdraw with a balance of 0.")
    else:
        balance -= withdraw
        print(f"Withdrew ${withdraw}. New balance: ${balance}.")
    return balance
    
def check_balance(balance):
    print(f"Your current balance is: ${balance}")

def main():
    print("Welcome to the ATM!")

    name = input("Please enter your name: ")
    balance = float(input("Enter your initial balance: $"))
    while True:
        option = display_main_menu()

        if option == 1:
            balance = deposit(balance)

        elif option == 2:
            balance = withdraw(balance)

        elif option == 3:
            check_balance(balance)

        elif option == 4:
            print(f"Goodbye, {name}! Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()