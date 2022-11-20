import random
#DONT change the code BELOW
test_seed = int(input("Type a seed number: "))
random.seed(test_seed)
#write your code below this line
random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
    