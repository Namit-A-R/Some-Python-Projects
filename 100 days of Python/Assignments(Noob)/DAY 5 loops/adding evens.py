# You are going to write a program that calculates the sum of all the even numbers 
# the user inputs the starting and ending number
starting_value = int(input("Enter the starting number: "))
ending_value = int(input("Enter the ending number: "))
sum = 0
for i in range(starting_value, ending_value+1):
      if i % 2 == 0:
          sum += i

print("The sum is: " , sum)
    
    