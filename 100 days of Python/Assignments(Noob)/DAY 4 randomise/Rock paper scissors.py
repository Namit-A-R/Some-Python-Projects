import random
import sys
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game = [rock, paper, scissors]
computer_choice = random.choice(game)

user_choice = int(input("1.rock\n2.paper\n3.scissors\nchoose(1,2,3): "))
if user_choice >= 4 or user_choice <= 0:
    sys.exit("Select a valid choice")
    
print("You chose: \n")
if user_choice == 1:
    user_choice = rock
    print(user_choice)
elif user_choice == 2:
    user_choice = rock
    print(user_choice)
else:
    user_choice = scissors
    print(user_choice)
    
print("Computer chose: \n")
print(computer_choice)

if user_choice == computer_choice:
    print("\n it is a draw")
elif (user_choice == rock and computer_choice == scissors) or (user_choice == paper and computer_choice == rock) or (user_choice == scissors and computer_choice == paper):
    print("You win!")
else:
    print("You lose!")



