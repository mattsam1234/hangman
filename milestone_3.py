import random

word_list = ["apple", "pear", "banana", "peach", "grape"]
word = random.choice(word_list)


        
def check_guess(user_guess):
    user_guess.lower()
    if user_guess in word:
        print(f"Good guess! {user_guess} is in the word.")
    else:
        print(f"Sorry, {user_guess} is not in the word. Try again.")

    
def ask_for_input():
    while True:
        user_guess = input("Please make a guess: ")
        if len(user_guess) == 1 and user_guess.isalpha():
            break
        else:
            print("This is not a valid guess")
    check_guess(user_guess)
    
ask_for_input()