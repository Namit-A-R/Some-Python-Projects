# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.

import math

def buy_cans():
    return math.ceil((height_of_wall*width_of_wall)/coverage)

height_of_wall = float(input("Enter wall Height: "))
width_of_wall = float(input("Enter wall Width: "))
coverage = float(input("Enter paint coverage per can: "))

print(f"Total number of cans required = {buy_cans()}")


    
