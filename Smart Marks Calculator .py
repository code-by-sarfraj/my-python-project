# 🚀 Project — Smart Marks Calculator

print("================================")
print("         STUDENT RESULT")
print("================================")

name = input("Enter Student Name: ")
hindi = int(input("Enter Hindi Marks: "))
english = int(input("Enter English Marks: "))
math = int(input("Enter Math Marks: "))
science = int(input("Enter Science Marks: "))
computer = int(input("Enter Computer Marks: "))

a = hindi + english + math + science + computer
percentage = (a / 500) * 100

print("================================")
print("         STUDENT RESULT")
print("================================")

print("Name       :", name)
print("Total      :",a,"/500")
print("Percentage :",percentage, "%" )

if a >= 420:
    print("Grade      :", "A")

elif a >= 330:
    print("Grade      :", "B")

elif a >= 250:
    print("Grade      :", "C")

elif a >= 220:
    print("Grade      :", "D")

else:
    print("Grade      :", "F")

if a >= 150:
    print("Result     :", "PASS")

else:
    print("Result     :", "FAIL")

print("================================")
