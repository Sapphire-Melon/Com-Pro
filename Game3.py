'''

Game 3
Guessing Word Game

'''

import random

Question = ("python", "yellow", "harmony", "monster", "nothing", "august", "future" ,"secret")

answer = random.choice(Question)

correct = answer
count = 3
rumble = ""

while answer:
    position = random.randrange(len(answer))
    rumble += answer[position]
    answer = answer[:position] + answer[(position + 1):]
print("Welcome to the Guessing word Game!")
print("")
print("you will have only 3 try for this game")
print("")
print("But remember this! the less you try, the more reward you will get")
print("")
print("then let's us start the game!")
print("")
print("The Question Is :", rumble)
print("You have", count, "more try")
guess = input("Guess The Word : ")
guess = guess.lower()

while count > 1 :
    if (guess != correct) or (guess == ""):
        print("")
        print("That is not the correct answer, Try again!")
        count = count - 1
        print("You have", count, "more try")
        guess = input("Guess The Word : ")
        guess = guess.lower()
    elif guess == guess :
        print("")
        print("Congratulation You Win!")
        print("Your score is: %d"%count)
        break
        
else :
    print("")
    print("Nice try but not nice enough!")
    print("git gud dude")