import random
import webbrowser
from graphics import hangman_pics   # imports the hangman graphics from the graphics.py file

class Hangman:
    ''' 
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with 5 lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    _check_guess(letter)
        Private method.
        Checks if the player's letter is in the word.
    _ask_for_input()
        Private method.
        Asks the player to guess a letter.        
    
    Returns:
        An interactive game mode as per the users inputs.
        If player guesses all the letters in the word in 5 lives, they win.
        Whereas if the player is not able to guess in 5 lives, they lose.
    '''
    
    def __init__(self, word_list, num_lives=5):             
        ''' 
        Initialises the attributes of the Hangman class.
        '''
        self.word_list = word_list              
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)          # _ for each letter of the word i.e. length of the word
        self.num_letters =  len(set(self.word))             # unique letters in the word that have not been guessed yet
        self.list_of_guesses = []                           # list of of guesses that have been tried, empty at start


    def _check_guess(self,guess):
        '''
        Checks if the guessed letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The player entered letter to be checked
        '''
                               
        guess = guess.lower()
        
        if guess in self.word:                              # checks if the Player's guess is in the word
            print(f"Good guess! {guess} is in the word.")

            for index in range(len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess        # adds the correct letter at the right position
            
            print(self.word_guessed)

            self.num_letters -=1

        else:
            self.num_lives -= 1                             # 1 life deducted
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            print(hangman_pics[5-self.num_lives])


    def _ask_for_input(self):
       '''
       Asks the user for a letter and checks two things:
       1. If the character is a single character and an albhabetic character
       2. If the letter has already been tried
       If it passes both checks, it calls the _check_guess method.
       '''
       while True:
            guess = input("Guess a letter: ")
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            elif guess in self.list_of_guesses:
                print(f"You have already tried {guess} before")
            
            else:
                self._check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    '''
    Runs the Hangman Game using the list of words.
    
    Parameters:
    ----------
    word_list : list
        List of words the program can randomly choose from.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("Oh no, all lives gone. You lost!")
            print(f"The correct word was \033[1m{game.word}\033[0m. Better luck next time.")
            break
        
        elif game.num_letters > 0:
            game._ask_for_input()

        else:
            print("Congratulations! You won the game!")
            show_winning_gif()
            break


def show_winning_gif():
    '''
    Opens a GIF when the player wins the game.
    '''
    gif_path = "7.hangman/hangman524/milestone_5.py/winning_dance.gif"
    webbrowser.open(gif_path)


word_list = ["cherry", "mango", "kiwi", "grapes", "jackfruit"]
play_game(word_list)


        