

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

if attempts == 3:
    print("❌ Too Many Wrong Attempts")
    print("Your Account Is Locked")

while True:

    Balance = 15000

    print("\n========================")
    print("        ATM MENU")
    print("========================")

    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Current Balance:", "₹", Balance)

    elif choice == 2:
        wid = int(input("Enter Your Amount: "))

        