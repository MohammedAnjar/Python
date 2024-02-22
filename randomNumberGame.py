import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit : ")
    if(userChoice == "Quit"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your choice was too small. Take a bigger guess...")
    else:
        print("your choice was too big. Take a smaller guess...")

print("----GAME OVER----")