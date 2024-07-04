import time

print("please enter your password: ")

time.sleep(5)

password = 2004
pin = int(input("enter your password: "))

balance = 5000
transaction_history = []

if pin == password:
    while True:
        print("""
1 == Balance
2 == Withdraw Balance
3 == Deposit Balance
4 == Transaction History
5 == Exit
""")
        try:
            option = int(input("please enter your choice: "))
        except ValueError:
            print("Please enter a valid option.")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")

        elif option == 2:
            withdraw_amount = int(input("please enter your withdraw amount: "))
            if withdraw_amount > balance:
                print("Insufficient funds.")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account.")
                print(f"Your updated balance is {balance}")
                transaction_history.append(f"Withdraw: {withdraw_amount}")

        elif option == 3:
            deposit_amount = int(input("please enter your deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account.")
            print(f"Your updated balance is {balance}")
            transaction_history.append(f"Deposit: {deposit_amount}")

        elif option == 4:
            print("Transaction History:")
            for transaction in transaction_history:
                print(transaction)

        elif option == 5:
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")

else:
    print("Wrong pin, please try again.")










                          




















       
