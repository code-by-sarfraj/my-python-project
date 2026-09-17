# 🚀 Project — Employee Salary Calculator 🔥

name = input("Enter Employee Name: ")
salary = int(input("Enter Basic Salary: "))

if salary >= 100000:
    bonus = 20
elif salary >= 50000:
    bonus = 15
elif salary >= 20000:
    bonus = 10
elif salary <= 20000:
    bonus = 5
else:
    bonus = 0

bonus_amount = salary * bonus / 100
final_salary = salary + bonus_amount

print("Employee Name :", name)
print("Basic Salary  :", salary)
print("Bonus         :", bonus, "%" )
print("Bonus Amount  :", bonus_amount)
print("Final Salary  :", final_salary)