import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0  
    while guess != random_number:
        guess = int(input(f'Guess A number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Its Too low.')
        elif guess > random_number:
            print('Sorry, Its Too High.')
        
    print('Congrats! You have Guessed it...')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could be high as high == low
        
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            pass
        else:
            print("Wrong Input.")
        


    print('The Computer Guessed Your Number.')



print("Welcome to Guess the Number Game!")

while True:
    print("1. You want to Guess the Number. OR\n2. Let computer Guess the Number.")
    option = int(input("Pick one Option OR (0 = Exit):. "))

    if option == 1:
        guess(100)
    elif option == 2:
        computer_guess(99)
    elif option == 0:
        break
    else:
        print("You Picked Wrong Number...")
