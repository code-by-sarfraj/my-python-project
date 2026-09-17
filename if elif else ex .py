# Q1 — Positive / Negative

a = int(input("Enter Any Number "))

if a > 0:
    print("Positive")

elif a < 0:
    print("Negative")

else:
    print("Zero")

# Q2 — Even / Odd

a = int(input("Enter Any Number "))

if a % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")

# Q3 — Pass / Fail

msk = int(input("Enter Your Mask "))

if msk >= 40:
    print("Pass")

else:
    print("fail")

# Q4 — Grade System

marks = int(input("Enter Your Marks: "))

if marks >= 90:
    print("Grade: A")

elif marks >= 80:
    print("Grade: B")

elif marks >= 70:
    print("Grade: C")

elif marks >= 60:
    print("Grade: D")

else:
    print("Grade: F")

# Q5 — Age Category

age = int(input("Enter Your Age: "))

if age <= 12:
    print("Category: Child")

elif age <= 19:
    print("Category: Teenager")

elif age <= 59:
    print("Category: Adult")

else:
    print("Category: Senior Citizen")

# Q6 — Largest Number

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a > b:
    print("Largest a")

elif b > c:
    print("Largest b")

else:
    print("Largest c")


a = int(input("Enter First Number: "))

b = int(input("Enter Second Number: "))

c = int(input("Enter Third Number: "))

if a > b and a > c:
    print("Largest =", a)

elif b > a and b > c:
    print("Largest =", b)

else:
    print("Largest =", c)