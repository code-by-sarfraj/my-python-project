# 🚀 Project — Advanced Table Generator


while True:


    print("=========================")
    print("     TABLE GENERATOR     ")
    print("=========================")

    print("1. Generate Table")
    print("2. Generate Multiple Tables")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        num = int(input("Enter Number: "))
        for i in range(1, 11):
         print(num, "x", i, "=", num * i)

    elif choice == 2:
       stnum = int(input("Enter Starting Number: "))
       ennum = int(input("Enter Ending Number: "))

       for num in range(stnum, ennum + 1):
          print("\nTable of", num)
          for i in range(1, 11):
             print(num, "x", i, "=", num * i)

    elif choice == 3:
       print("Thank you!")
       break

    else:
       print("Invalid choice!")