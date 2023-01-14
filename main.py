from random import *
number = randint(0, 5)
print('Guess the number (0 to 5)')
guess = input()
while int(guess) != number:
    print('You was close! Try another one \n'
          'Type N if you want to stop the game and see the number')
    guess = input()
    if guess == 'N':
        print(f'The number was {number}. You did good!')
        break
    elif int(guess) == number:
        print(f'You did it! The number was {number}')