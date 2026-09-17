# 🚀 Project — ATM Mini System

balance = 10000

print("===== ATM =====")
print("1. Check Balance")
print("2. Withdraw Money")
print("3. Deposit Money")

choice = int(input("Enter Choice: "))

if choice == 1:
    print("Your Balance = ₹", balance)

elif choice == 2:
    amount = int(input("Enter Your Amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Please collect your cash")
        print("Remaining Balance =", balance)

    else:
        print("Insufficient Balance")

elif choice == 3:
    dep = int(input("Enter Your Deposit Money: "))
    balance = balance + dep
    print("New Balance =", balance)

else:
    print("Invalid Choice")