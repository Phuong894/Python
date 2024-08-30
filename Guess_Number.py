import random

secret = random.randint (0,100)
#assigns variable "secret" a random value between 0 and 100
name = input('what is your name? ')
#ask user for their name
guess = int(input('choose a number between 1 and 100 ' + name ))
#ask user to input a number between 1 and 100
while guess != secret: #starts loop when user's guess is not equal to secret number
    if guess < secret:
        print ('guess is too low')
    else:
        print('Guess is too high')
    guess = int(input ('Choose a number between 1 and 100 again '))
print ('You got it correct! :) ') #exit the loop when guess is correct
