'''
Collaborators: None

Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''

import random

x = random.randint(1,11)

number_of_guesses = 0
while number_of_guesses < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    number_of_guesses = number_of_guesses + 1
    if guess > x:
        print("Your number is too high.")
    elif guess < x:
        print("Your number is too low.")
    else:
        print("Your guess is correct!")
        break
