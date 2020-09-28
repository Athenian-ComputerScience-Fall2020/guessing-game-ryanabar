'''
Collaborators: None
'''

def rerun(): 
	while True: 
		guessing_game() 

def guessing_game():        
    import random

    low = int(input("Enter a minimum boundary for the range of numbers: "))
    high = int(input("Enter a maximum boundary for the range of numbers: "))
    x = random.randint(low, high)

    try:
        number_of_guesses = 0
        while number_of_guesses < 1000000000000000000:
            guess = int(input("Guess a number between your minimum and your maximum boundaries or press 'q' to quit: "))
            number_of_guesses = number_of_guesses + 1
            if guess == str("q"):
                break
            if guess > x:
                print("Your number is too high.")
            elif guess < x:
                print("Your number is too low.")
            else:
                print("Your guess is correct!")
                break
    except:
        print("Please enter a number.")

if __name__ == '__main__': 
    rerun() 



'''
I no longer need this code because you can't run out of guesses anymore.

if number_of_guesses == 5:
            print("I'm sorry, you are out of guesses.")
            print("\n")
        if number_of_guesses == 4:
            print("I'm sorry you are giving up!")
            print("\n")
'''