import math
import random

def mysqrt(a):
    '''
    Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that
    takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a.
    '''
    
    x = 3
    y = (x + a / x) / 2
    
    print(y)

mysqrt(6)

def eval_loop():
    '''
    Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
    evaluates it using eval, and prints the result.
    '''
    while True:
        user = input("Enter an expression: ")
        
        x = eval(user)    
        print("Result: ", x)
        
        print('\n Are you done? Type done if yes')
        exit = input('_ ')
        
        if exit.lower() == 'done':
            break
    
    
eval_loop()

'''
guess_number = random.randint(1, 10)

while True:
    user_guess = input('Guess the number between 1 and 10: ')
    
    if int(user_guess) == guess_number:
        print('You guessed it!')
        break

    elif int(user_guess) < guess_number:
        print('Too low, guess again again')
        
    elif int(user_guess) > guess_number:
        print('Too high, guess again')
'''

computer_guess = random.choice(['r', 'p', 's'])

while True:
    user_guess = input('Enter r for rock, p for paper, s for scissors: ')
    
    if user_guess == computer_guess:
        print('It\'s a tie!')
    
    elif (user_guess == 'r' and computer_guess == 's') or (user_guess == 's' and computer_guess =='p') or (user_guess == 'p' and computer_guess == 'r'):
        print('------')
        print('User wins!! :)')
    
    else:
        print('Aww you lose :(')
    
    exit = input('>>')
    if exit.lower() == 'done':
        break
    
 
    

