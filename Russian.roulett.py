import random
import os
os.system('reboot')

def game():
    
    num1 = input("Enter a number between 1-6: ")

    num2 = random.randint(1, 6)
    if int (num1) > 6:
        print("That's higher than the number 6")
        quit()
    
    elif int(num1) == int (num2):
        choose = input ("You died, do you want to restart?(y or n)")
        if choose == "y":
            print("Shutting down")
            os.system("shutdown /r /t  1")
        elif choose == "n":
            print("quitting")
            quit()
        else:
            print("did not reckognize input quitting.")
            quit()
            
    elif int (num1) != int (num2):
        print("You have surived, the number was", num2 ,"Lucky bastard")
        quit()
    
        

game()
