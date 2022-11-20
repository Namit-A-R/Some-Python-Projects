import random
import sys
import os
from hangman_art import stages,logo
from word_list import words

random_word = random.choice(words)

random_word_length = len(random_word)

blank = "_"

for word in range(random_word_length - 1):
    blank += " _"
life = 6
wrong_guess = 0
continuation = "y"
while(continuation == "y"):
    blank_copy = blank          
    print(logo)
    print(stages[life])
    
    if wrong_guess == 1:
        print("You guessed the wrong word.")
        wrong_guess = 0
        
    print(f"\nYou have {life} lives remaining")
    print("\n",blank , "\n")
    user_guess_word = input("Guess a word: ")
    guessed_words = []
    guessed_words.append(user_guess_word)
    
    for i in range(random_word_length):
        
        if user_guess_word == random_word[i]:

            blank = blank.split()
            blank[i] = user_guess_word
            blank_copy_copy = " "
            blank = blank_copy_copy.join(blank)
        
            if blank.replace(" ","") == random_word:
                sys.exit("You Win\n")
                
    def clear(): return os.system('cls')
    clear(),
    
    if blank_copy == blank:
        life -= 1
        wrong_guess = 1
        
    if life == 0:
        clear(),
        print(logo)
        print(stages[life])
        print(f"\nYou have {life} lives remaining")
        print("You Lose\n")
        continuation = input("Do you want to try again?:(y,n): ").lower()

    
    
    
