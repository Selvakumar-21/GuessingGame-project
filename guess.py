import random

#generate a random number between 1 to 100

number = random.randint(1,100)

#set the intial number of guesses to 0
num_guesses = 0
print("I'm thinking of a number between 1 to 100.can you guess what it is?")

while(True):
    #Ask the user to guess the Number
    guess = int(input("Enter your Guess: "))
    
    #increment the Numberof Guesses
    num_guesses=num_guesses+1
    
    #check if the guess is correct
    if(guess == number):
        print("Congratulations,you guessed the number in",num_guesses,"guesses!")
        break
        
    elif(guess < number):
        print("Your guess is too low. Try again..")
        
    else:
        print("Your guess is too High. Try again..")
    