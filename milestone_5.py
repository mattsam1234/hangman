import random

class Hangman:
    '''The Hangman class contains all the logic needed to play a game of hangman. When initialised it needs a list of words and optionally an intiger for the number of lives the player has
    The ask_for_input method can be called to request the user input a letter and will then validate the letter and check if it is in the word.'''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = []
        for character in self.word:
            self.word_guessed.append("_")
        print(self.word_guessed)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def __check_guess(self, guess):
        '''This function checks is the guess is in the global scope variable word and then updates the word_guessed list with the letter at all positions it appears if the guess is correct'''
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")
            
    def ask_for_input(self):
        '''Asks user for input and then validates the input and checks if it is in the chosen word.'''
        guess = input("Please make a guess: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
                
def play_game(word_list):
    '''Complete game function which takes a word_list then continues or ends game based on winning or losing conditions'''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives > 0 and game.num_letters == 0:
            print("Congrats you won")
            break

play_game(["apple", "pear", "banana", "peach", "grape"])