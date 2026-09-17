# 🚀 Project — Movie Ticket Booking 🎬

age = int(input("Enter Your Age: "))
ticket = int(input("Enter Tickets: "))

Price = 200

if age <= 5:
    Discount = 100
elif age <= 12:
    Discount = 50
elif age <=  59:
    Discount = 0
elif age >= 60:
    Discount = 30
else:
    print("Discount = 20")

total = ticket * 200
dis = total * Discount / 100
fainal = total - dis

print("Ticket Price : ₹200")
print("Discount     :", Discount, "%")
print("Final Amount :", fainal)