# # 🚀 Project — Student Marks Management System

while True:

    print("==============================")
    print("   STUDENT MARKS MANAGEMENT   ")
    print("==============================")

    students = int(input("How many students: "))

    for i in range(students):
         print("Student:", i + 1)

         name = input("Name: ")
         math = int(input("Math: "))
         english = int(input("English: "))
         science = int(input("Science: "))

         total = math + english + science
         percentage = total / 3

        
         if percentage >= 90:
           grade = "A+"
         elif percentage >= 80:
           grade = "A"
         elif percentage >= 70:
           grade = "B"
         elif percentage >= 60:
           grade = "C"
         elif percentage >= 50:
           grade = "D"
         else:
           grade = "E"

         if math < 33 or english < 33 or science < 33:
          result = "FAIL"
         else:
          result = "PASS"


         print("==============================")
         print("Student:", name)
         print("Total:", total, "/ 300")
         print("Percentage:", round(percentage, 2), "%")
         print("Grade:", grade)
         print("Result:", result)
         print("==============================")

    print("Do you want to enter another batch?")
    print("1. Yes")
    print("2. No")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        continue
    elif choice == 2:
        print("==============================")
        print("          Thank you!          ")
        print("==============================")
        break
    else:
        print("Invalid Choice")
        break
