import random
import sys


def guess_a_number(computer_number):
    global life_chance, win
    user_number = int(input("Guess a number: "))
    if user_number == computer_number:
        print("You win")
        win = True
    elif user_number > computer_number:
        print("Value is High")
        life_chance -= 1
    else:
        print("Value is Low")
        life_chance -= 1


play_again = "y"
win = False

while play_again == "y":
    computer_number = random.randint(0, 100)
    difficulty = int(input("Select \n1.Easy\n2.Hard: "))

    if difficulty == 1:
        life_chance = 10
    elif difficulty == 2:
        life_chance = 5
    else:
        sys.exit("Invalid difficulty")

    while life_chance != 0:
        guess_a_number(computer_number)
        if win == True:
            break
        print(f"You have {life_chance} lives remaining")
        if life_chance == 0:
            print("you lose")

    play_again = input("Do you want to play_again?: ").lower()
