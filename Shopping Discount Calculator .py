# 🚀 Project — Shopping Discount Calculator 🛒

amount = int(input("Enter Shopping Amount: "))


if amount >= 10000:
    Discount = 20
elif amount >= 5000:
    Discount = 10
elif amount >= 1000:
    Discount = 5
else:
    Discount = 0

Dis = amount * Discount / 100

fainal = amount - Dis

print("Original Amount :", amount)
print("Discount        :", Discount, "%")
print("Discount Amount :", Dis)
print("Final Amount    :", fainal)