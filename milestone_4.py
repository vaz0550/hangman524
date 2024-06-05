import random

class HangMan:
    def __init__(self, word_list, num_lives=5):
        ''' Initialises the attributes of the Hangman Class
        Args: 
            word_list is a list of words
            num_lives is the no. of lives the player has,
            set to 5 at the start of the game.
        Returns:
            None?
        '''
        self.word_list = word_list              
        self.num_lives = num_lives
        self.word = random.choice(word_list)
 #       print(self.word)                                   # for testing, to be deleted
        self.word_guessed = ['_'] * len(self.word)          # _ for each letter of the word i.e. length of the word
        self.num_letters =  len(set(self.word))             # unique letters in the word that have not been guessed yet
        self.list_of_guesses = []                           # list of of guesses that have been tried, empty at start


    def check_guess(self,guess):                     
        guess = guess.lower()
        
        if guess in self.word:                              # checks if the Player's guess is in the word
            print(f"Good guess! {guess} is in the word.")

            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess        # adds the correct letter at the right position

            self.num_letters -=1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    
    def ask_for_input(self):                    # asks for & validates (single char & alphabet) input from the user
        while True:
            guess = input("Guess a letter: ")
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            elif guess in self.list_of_guesses:
                print(f"You have already tried {guess} before")
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


word_list = ["cherry", "mango", "kiwi", "grapes", "jackfruit"]
game1 = HangMan(word_list)
x = game1.ask_for_input()


        