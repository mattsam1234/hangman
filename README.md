# Hangman

## Table of contents

1. Description of project
2. Variables and names
3. Functions

### The project

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

### Variables:

1. word_list : The list of words that the computer can choose from
2. num_lives : The number of guessed the player has before losing
3. word : The word randomly chosen from the list
4. word_guessed : List of \* made to represent the amount of letters in the word
5. num_letters : The amount of unique letters in the word
6. list_of_guesses : list of letters that have been guessed previously

### Functions:

1. The class for Hangman is called
2. **init** method initialises all the variables
3. check_guess() takes the users guess and checks whether it is in the word
4. ask_for_input() geta the user to input a letter. If the letter is invalid, a new guess will be asked for. If its valid then it runs the check_guess() function

### My Experience doing this

I found this project to be built up in a strange way.
In terms of the milestones i would have expected to slowly build up the functionality in functions then bring it all together layer by layer.

I personally need to get better at testing my greater than and less than checks as have found i often get them confused.

During the project i had to look up how to get the index position of a variable in a for loop.
This was where i used the enumerate function in the check_guess() function.

Overall this project for me was more of a learning curve by documenting the progress in the README file.
As for the complexity of the project overall this was a fairly easy project.
