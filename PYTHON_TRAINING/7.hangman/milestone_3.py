import random

word_list = ["cherry", "mango", "kiwi", "grapes", "jackfruit"]

word = random.choice(word_list)         # program chooses a fruit at random


def check_guess(guess):                 # converts the guess in lower case and checks if in the random word
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():                    # asks for & validates (single char & alphabet) input from the user
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()




