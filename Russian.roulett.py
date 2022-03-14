import random

def game():
    
    num1 = input("Enter a number between 1-6: ")

    num2 = random.randint(1, 6)
    if int (num1) > 6:
        print("That's higher than the number 6")
        quit()
    
    elif int(num1) == int (num2):
        print ("You died, better luck next time")
        quit()

    elif int (num1) != int (num2):
        print("You have surived, the number was", num2 ,"Lucky bastard")
        quit()
    
        

game()