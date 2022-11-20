# Problem: based on users order work out their final bill:
# small pizza: $15
# medium pizza: $20
# large pizza: $25

# peporoni for small pizza: +$2
# pepperoni for medium and large pizza: +$3

# extra cheese for any size pizza: +$1

#DO NOT CHANGE THE CODE BELOW
print("Welcome to python pizza :)")
size = input("What size do you want? S,M,L : ")
add_pepperoni = input("Do you need pepperoni?Y,N: ")
extra_cheese = input("Do you need extra cheese?Y,N: ")
#UNTIL HERE
add_pepperoni = add_pepperoni.casefold()
extra_cheese = extra_cheese.casefold()
size = size.casefold()

if size == "s":
    bill = 15
    if add_pepperoni == "y":
        bill += 2
   
else:
    bill = 20
    if size == "l":
        bill = 25
    if add_pepperoni == "y":
        bill += 3

if extra_cheese == "y":
    bill += 1 
    
print(f"Your order costs: ${bill}")

