import random
userInput = input("Chose heads or tails(case-senstive).\n")
if userInput == "heads":
    userInput = 1
elif userInput == "tails":
    userInput == 2
else:
    print("Invaild choice. Check your speeling. Remember, it is case-sensitive!")
    exit()

compInput = random.randint(1, 2)
if compInput == 1:
    print("Heads")
else:
    print("Tails")