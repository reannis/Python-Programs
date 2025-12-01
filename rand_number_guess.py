import random

newmax = input('set the maximum value to: ')

amount = 0

newmax = int(newmax)

guess = 0

number = random.randrange(1, newmax, 1)

while guess != number:
    guess = int(input('guess the number '))
    if guess > number:
        print('lower')
        amount = amount + 1
    elif guess < number:
        print('greater')
        amount = amount + 1

amount = amount + 1
print('congrats you guessed it!')

if amount == 1:
    print('it took you 1 guess')
else:
    print('it took you',amount, 'guesses')
