'''
Collaborators: Megan
'''

def guessing_game(): #Defining my function
    import random

    low = int(input("Enter a minimum boundary for the range of numbers: ")) #Lower boundary input from user
    high = int(input("Enter a maximum boundary for the range of numbers: ")) #Upper boundary input from user
    x = random.randint(low, high)

    try:
        max_guess = int(input("How many guesses would you like to have? ")) #Number of guesses input from user
        number_of_guesses = 0
        while number_of_guesses < max_guess:
            guess = int(input("Guess a number between your minimum and your maximum boundaries or press 'q' to quit: ")) #Where user enters their guess
            number_of_guesses = number_of_guesses + 1
            if guess == str("q"): #Quits the program
                break
            if guess > x: #Guess is too high
                print("Your number is too high.")
            elif guess < x: #Guess is too low
                print("Your number is too low.")
            else: #Correct guess
                print("Your guess is correct!")
                break
    except: #If the user does not enter a number...
        print("Please enter a number.")

if __name__ == '__main__': 
    guessing_game() #Calling the function
    while True:
        a = input("Play again? Please say yes or no. ") #Option to play again
        if a == "yes": #Plays again
            guessing_game()
        if a == "no": #Does not play again
            break



'''
I no longer need this code because you can't run out of guesses anymore.

if number_of_guesses == 5:
            print("I'm sorry, you are out of guesses.")
            print("\n")
        if number_of_guesses == 4:
            print("I'm sorry you are giving up!")
            print("\n")
'''