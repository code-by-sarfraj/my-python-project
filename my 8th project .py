username = input("Enter your username: ")

if len(username) < 5:
    print("Invalid Username")

elif username.isspace():
    print("Invalid Username")

elif username.isalpha():
    print("Valid Username")

else:
    print("Invalid Username")