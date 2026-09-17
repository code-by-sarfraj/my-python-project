# 🚀 Project — Number Guessing Game 🎮

secret_number = 47
attempts = 0

while True:

    print("================================")
    print("      NUMBER GUESSING GAME      ")
    print("================================")

    print("Guess a number between 1 and 100")

    while True:

      guess = int(input("Enter Your Guess: "))

      attempts = attempts + 1

      if guess > secret_number:
        print("Too Low! 🔻")

      elif guess < secret_number:
        print("Too High! 🔺")

      elif guess == secret_number:
        print("🎉 Correct!")
        break


    print("You guessed it in", attempts, "attempts!")
    print("-------------------------------")
    print("1. Play Again")
    print("2. Exit")
    print("-------------------------------")



    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        continue

    elif choice == 2:
        print("Thank You for Playing! 🎮")
        break
    else:
       ("Invalid Choice!")