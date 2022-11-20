import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password Genarator")
number_of_letters = int(input("How many letters would you like?: "))
number_of_numbers = int(input("How many numbers would you like?: "))
number_of_symbols = int(input("How many symbols would you like?: "))
password = ""

for letter in range(0, number_of_letters):
    password += random.choice(letters)

for number in range(0, number_of_numbers):
    password += random.choice(numbers)

for symbol in range(0, number_of_symbols):
    password += random.choice(symbols)

password = "".join(random.sample(password, number_of_symbols+number_of_numbers+number_of_letters))
print(f"Your password is: {password}")
