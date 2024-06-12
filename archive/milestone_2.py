import random

word_list = ["cherry", "mango", "kiwi", "grapes", "jackfruit"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess")
    print("\N{smiling face with halo}")
else:
    print("Oops! That is not a valid input.")
    print("\N{unamused face}")
    