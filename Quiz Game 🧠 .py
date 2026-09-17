# 🚀 PROJECT 7 — Python Quiz Game 🧠

while True:

    score = 0

    print("========================")
    print("       PYTHON QUIZ")
    print("========================")

    # Q1
    print("\nQ1. Python kis type ki language hai?")
    print("A. Programming")
    print("B. Markup")
    print("C. Styling")
    print("D. Database")

    answer = input("Enter Answer: ").upper()

    if answer == "A":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong!")
        print("Correct Answer: A")

    print("Score:", score)

    # Q2
    print("\nQ2. Python file ka extension kya hota hai?")
    print("A. .html")
    print("B. .py")
    print("C. .css")
    print("D. .java")

    answer = input("Enter Answer: ").upper()

    if answer == "B":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong!")
        print("Correct Answer: B")

    print("Score:", score)

    # Q3
    print("\nQ3. Python mein output ke liye kya use hota hai?")
    print("A. input()")
    print("B. print()")
    print("C. output()")
    print("D. display()")

    answer = input("Enter Answer: ").upper()

    if answer == "B":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong!")
        print("Correct Answer: B")

    print("Score:", score)

    # Q4
    print("\nQ4. Python mein comment ke liye kya use hota hai?")
    print("A. //")
    print("B. <!-- -->")
    print("C. #")
    print("D. **")

    answer = input("Enter Answer: ").upper()

    if answer == "C":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong!")
        print("Correct Answer: C")

    print("Score:", score)

    # Q5
    print("\nQ5. Python mein list kis bracket se banti hai?")
    print("A. ()")
    print("B. {}")
    print("C. []")
    print("D. <>")

    answer = input("Enter Answer: ").upper()

    if answer == "C":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong!")
        print("Correct Answer: C")

    print("Score:", score)

    # Q6
    print("\nQ6. Python mein loop ke liye kya use ho sakta hai?")
    print("A. for")
    print("B. loop")
    print("C. repeat")
    print("D. again")

    answer = input("Enter Answer: ").upper()

    if answer == "A":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong!")
        print("Correct Answer: A")

    print("Score:", score)

    # Q7
    print("\nQ7. Python mein condition check karne ke liye kya use hota hai?")
    print("A. if")
    print("B. check")
    print("C. condition")
    print("D. when")

    answer = input("Enter Answer: ").upper()

    if answer == "A":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong!")
        print("Correct Answer: A")

    print("Score:", score)

    # Q8
    print("\nQ8. Python mein user se input lene ke liye kya use hota hai?")
    print("A. get()")
    print("B. input()")
    print("C. scan()")
    print("D. read()")

    answer = input("Enter Answer: ").upper()

    if answer == "B":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong!")
        print("Correct Answer: B")

    print("Score:", score)

    # Q9
    print("\nQ9. Python mein dictionary kis bracket se banti hai?")
    print("A. []")
    print("B. ()")
    print("C. {}")
    print("D. <>")

    answer = input("Enter Answer: ").upper()

    if answer == "C":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong!")
        print("Correct Answer: C")

    print("Score:", score)

    # Q10
    print("\nQ10. Python kisne banayi?")
    print("A. Elon Musk")
    print("B. Guido van Rossum")
    print("C. Bill Gates")
    print("D. Mark Zuckerberg")

    answer = input("Enter Answer: ").upper()

    if answer == "B":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong!")
        print("Correct Answer: B")

    print("Score:", score)

    # Final Result
    wrong = 10 - score
    percentage = (score / 10) * 100

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

    print("\n========================")
    print("        RESULT")
    print("========================")

    print("Correct Answers :", score)
    print("Wrong Answers   :", wrong)
    print("Final Score     :", str(score) + "/10")
    print("Percentage      :", percentage, "%")
    print("Grade           :", grade)

    print("========================")

    print("1. Play Again")
    print("2. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        continue

    elif choice == 2:
        print("Thank You For Playing! 🧠")
        break

    else:
        print("Invalid Choice!")
        break