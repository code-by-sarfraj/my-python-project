# 🚀 Project — ATM Banking System

# balance = 10000
# transactions = []

# while True:
#     print("=====================")
#     print("         ATM         ")
#     print("=====================")
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Transaction History")
#     print("5. Exit")
#     print("=====================")

#     choice = int(input("Enter Your Choice: "))

#     if choice == 1:
#         print("---------------------")
#         print("Current Balance: ₹", balance)
#         print("---------------------")

#     elif choice == 2:
#         dep =int(input("Enter Deposit Amount: "))
#         depamount = balance + dep
#         print("Deposit Successful")
#         print("Current Balance: ₹", depamount)


#     elif choice == 3:
#         withdraw = int(input("Enter Withdraw Amount:" ))
#         wid = balance - withdraw
#         print("Withdrawal Successful")
#         print("Remaining Balance: ₹", wid)

#     elif choice == 4:
#         print("=====================")
#         print("  TRANSACTION HISTORY")
#         print("=====================")

#         if len(transactions) == 0:
#                     print("No Transactions Yet")
#         else:
#              for i in range(len(transactions)):
#                   print("Transaction", i + 1, ":", transactions[i])


    # elif choice == 5:
    #     print("Thank you for using ATM!")
    #     print("Have a nice day 😊")
    #     break

    # else:
    #     print("Invalid choice!")
    #     print("Please select between 1 and 5.")
    

# 🚀 Project 2 — ATM Banking System

balance = 10000
transactions = []

while True:

    print("\n=====================")
    print("        ATM")
    print("=====================")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")
    print("=====================")

    choice = int(input("Enter Your Choice: "))

    # 1. Check Balance
    if choice == 1:

        print("\n---------------------")
        print("Current Balance: ₹", balance)
        print("---------------------")

    # 2. Deposit
    elif choice == 2:

        amount = int(input("\nEnter Deposit Amount: ₹"))

        if amount <= 0:
            print("Invalid Amount")

        else:
            balance = balance + amount
            transactions.append("Deposited ₹" + str(amount))

            print("\nDeposit Successful")
            print("Current Balance: ₹", balance)

    # 3. Withdraw
    elif choice == 3:
       
        amount = int(input("\nEnter Withdraw Amount: ₹"))

        if amount <= 0:
            print("Invalid Amount")

        elif amount > balance:
            print("Insufficient Balance")

        else:
            balance = balance - amount
            transactions.append("Withdrawn ₹" + str(amount))

            print("\nWithdrawal Successful")
            print("Remaining Balance: ₹", balance)

    #  4. Transaction History
    elif choice == 4:

        print("\n=====================")
        print("  TRANSACTION HISTORY")
        print("=====================")

        if len(transactions) == 0:
            print("No Transactions Yet")

        else:
            for i in range(len(transactions)):
                print("Transaction", i + 1, ":", transactions[i])

    # 5. Exit
    elif choice == 5:

        print("\nThank you for using ATM!")
        print("Have a nice day 😊")
        break

    # Invalid Choice
    else:
        print("\nInvalid Choice")
        print("Please select between 1 and 5.")