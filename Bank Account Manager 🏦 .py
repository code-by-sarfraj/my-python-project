# 🚀 PROJECT — Bank Account Manager 🏦

balance = 25000

while True:

    print("========================")
    print("      BANK ACCOUNT")
    print("========================")

    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Loan Eligibility")
    print("5. Exit")

    print("========================")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("---------------------")
        print("Current Balance: ₹", balance)
        print("---------------------")

    elif choice == 2:
        dep = int(input("Enter Your Deposit Money: "))

        depamount = dep + balance
        print("Deposit Successful")
        print("Current Balance: ₹", depamount)

    elif choice == 3:
        widamount  = int(input("Enter Withdraw Amount:"))

        wid = balance - widamount
        print("Withdraw Successful")
        print("Current Balance: ₹", wid)

        if widamount <= balance:
            print("Withdraw Successful")

        else:
            print("insufficient Balance")

    elif choice == 4:
        age = int(input("Enter Your Age: "))
        salary = int(input("Enter Your Salary: "))

        if age >= 21 and age <= 60 and salary >= 30000:
            print("Eligible")
        else:
            print("Not Eligible")

    elif choice == 5:
        print("Thank You For Using Our Bank! 🏦")
        print("Have a nice day 😊")
        break

    else:
        print("Invalid Choice")
        print("Please select between 1 and 5.")