numbers = []
for number in range(1,101):
    numbers.append(number)

even_numbers = [even for even in numbers if number%2 == 0]

print(even_numbers)

