import random
from words import words
import string

def get_valid_word(words):
    random_word = random.choice(words)
    while ('-' in random_word) or (' ' in random_word):
        random_word = random.choice(words)

    return random_word.upper()


# print(get_valid_word(words))

def hangman():
    word = get_valid_word(words)
    words_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letter = set()
    lives = 7 # user has 7 lives

    # get user input
    while len(words_letters) > 0:
        # for blank Space
        print()

        # print Lives
        print(f'Lives remaining: {lives}')
        
        # Mentioning the life reminaing
        if lives == 0:
            return print(f'You Lost! the word was {word.upper()}')

        # letter used
        print('You have used these letters :', ' '.join(used_letter))

        # what current word is (ie. W - R D)
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current Word : ', ' '.join(word_list))

        user_letter = input('Guess a Letter: ').upper()

        # proper letter entered
        if user_letter in alphabets - used_letter:
            used_letter.add(user_letter)
            # for correct guess
            if user_letter in words_letters:
                words_letters.remove(user_letter)
            else:
                lives -= 1
            
        # Already Guess word    
        elif user_letter in used_letter:
            print("Invalid Guess. You already Guess that Letter.")
        
        else:
            print("Invalid Character. try again")
    
    print('Congrats! The Word was : ', ' '.join(word))
        

hangman()