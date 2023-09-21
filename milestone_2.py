import random

word_list = ["apple", "pear", "banana", "peach", "grape"]
print(word_list)

word = random.choice(word_list)
print(word)

user_guess = input("Choose a letter: ")

if len(user_guess) == 1 and user_guess.isalpha():
    print("Good Guess")
else: 
    print("not valid")
    