# 🚀 Project — Mini Shop Billing System 🛒

while True:

    print("========================")
    print("       MINI SHOP")
    print("========================")

    print("1. Add Items")
    print("2. View Bill")
    print("3. Checkout")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        item = int(input("How many items: "))

        total = 0

        for i in range(1, item + 1):
            price = int(input("Item "  + str(i) +  " Price: "))
            quantity = int(input("Item "  + str(i) +  " Quantity: "))

            item_total = price * quantity
            total = total + item_total

        print("Items Added Successfully! ")

        if total >= 10000:
            Discount = 15
        elif total >= 5000:
            Discount = 10
        elif total >= 1000:
            Discount = 5
        else:
            Discount = 0
    
        dis = total * Discount / 100

    elif choice == 2:
        print("========================")
        print("     CURRENT BILL")
        print("========================")

        print("Total =", total - dis)

    elif choice == 3:
        print("========================")
        print("       FINAL BILL")
        print("========================")
        print("Total Amount    :", total)
        print("Discount        :", Discount, "%")
        print("Discount Amount :", dis)
        print("Final Amount    :", total - dis)
        print("========================")
        print("Thank You For Shopping! ")

    elif choice == 4:
        print("Thank You! Visit Again 🛒")
        break
    else:
        print("Invalid Choice!")