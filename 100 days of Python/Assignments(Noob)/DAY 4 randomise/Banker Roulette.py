#you are going write a program to pick a random name from a list of names, the person will need
#to pay everyones bill

#you are not allowed to use the choice function
import random

names  = input("Enter all the names seperated by a comma and a space: ")
name_list = names.split(", ")
random_number = random.randint(1, len(name_list))
random_name = name_list[random_number-1]
print(f"The person who will pay the bill is: {random_name}")
