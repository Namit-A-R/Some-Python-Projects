print("Welcome to the tip calculator")
bill = input("What was the total bill?: $")
bill = float(bill)
tip_percentage = int(input("what percentage tip would like to give?: "))

if(tip_percentage>0):
    tip = bill/tip_percentage
else:
    tip = 0
    
friends = int(input("How many people to split the bill?: "))
total = tip + bill
each = total/friends
print(f"The total bill is: ${total}")
print(f"Each person should pay: ${each}")

