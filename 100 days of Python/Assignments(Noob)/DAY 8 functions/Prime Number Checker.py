def one_and_two_and_three():
    if user_number != 2 and user_number != 3 and user_number != 1:
        prime_number_checker()
    elif user_number == 1:
        print(f"The number {user_number} is not a prime number")
    else:
        print(f"The number {user_number} is a prime number")


def prime_number_checker():
    not_prime = 0
    for number in range(2, user_number):
        if user_number % number == 0:
            print(f"The number {user_number} is not a prime number")
            not_prime = 1
            break
    if not_prime == 0:
        print(f"The number {user_number} is a prime number")


user_number = int(input("Enter any number: "))
one_and_two_and_three()
