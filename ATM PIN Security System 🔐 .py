# 🚀 PROJECT  — ATM PIN Security System 🔐

print("========================")
print("        ATM LOGIN")
print("========================")

pin = 1111
attempts = 0

while attempts < 3:

    user_pin = int(input("Enter PIN: "))

    if user_pin == pin:
        print("✅ Login Successful")
        break

    else:
        attempts = attempts + 1
        print("❌ Wrong PIN")

        attempts_left = 3 - attempts
        print("Attempts Left:", attempts_left)


# Account Lock Check

if attempts == 3:

    print("❌ Too Many Wrong Attempts")
    print("Your Account Is Locked")

else:

    # ATM starts only after successful login

    balance = 15000
    transactions = 0

    while True:

        print("\n========================")
        print("        ATM MENU")
        print("========================")

        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            print("Current Balance: ₹", balance)

        elif choice == 2:

            amount = int(input("Enter Withdraw Amount: "))

            if amount > 0 and amount <= balance:

                balance = balance - amount
                transactions = transactions + 1

                print("Withdrawal Successful")
                print("Remaining Balance: ₹", balance)
                print("Total Transactions:", transactions)

            else:

                print("Insufficient Balance")

        elif choice == 3:

            amount = int(input("Enter Deposit Amount: "))

            if amount > 0:

                balance = balance + amount
                transactions = transactions + 1

                print("Deposit Successful")
                print("New Balance: ₹", balance)
                print("Total Transactions:", transactions)

            else:

                print("Invalid Deposit Amount")

        elif choice == 4:

            print("========================")
            print("       THANK YOU")
            print("========================")

            print("Transactions:", transactions)

            break

        else:

            print("Invalid Choice!")
            print("Please select between 1 and 4.")
