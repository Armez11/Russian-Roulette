import random

def game():
    num1 = input ("Choose a number between 1-6: ")
    num2 = random.randint(1, 6)
    if int(num1) > 6:
        print ("You have entered a number higher than 6")
        quit()
    if int(num1) == int(num2):
       choose = input("you have died, do you want to try again (Y or N)")
       if choose == "y":
             print ("restarting...")
             quit()
    elif int(num1) != int(num2):
        print ("you won, the number was ", num2)
game()
