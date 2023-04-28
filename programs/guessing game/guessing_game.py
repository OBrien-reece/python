# Create a random number
# Determine the number of times the user is allowed to guess
# Initialize the guess counter to 0
# if the user guesses the correct number they win and if they
# maximize the trials and still haven't guessed the correct number, they lose
import random

secret_number = random.randint(1,10)
guess_counter = 0
guess_limit =3

while guess_counter < guess_limit:
    guess = int(input('Guess a random number: '))
    guess_counter += 1
    if guess == secret_number:
        print('You have successfully won the lottery')
        break
else:
    # secret_number = random.randint(1, 10)
    print('Ooops! You failed')

