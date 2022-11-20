# problem: Design a love calculator.
# insert the names of both parties and count the number of times the words T,R,U,E occur in
# both of your names and add them, thats the first digit.
# then count the number of times the words L, O, V, E occur in both of your names and add them,
# thats the Second digit.
# combine the two digits togather and you are all set to go.

# Dont change the code below
print("Welcome to the love calculator")
name1 = input("Enter your name: ")
name2 = input("what is the name of your love: ")
# Write your code below this line
name1 = name1.lower()
name2 = name2.lower()
count1 = 0
count2 = 0
for i in range(0,len(name1)):
    if name1[i] == "t" or name1[i] == "r" or name1[i] == "u" or name1[i] == "e":
        count1 += 1
    if name1[i] == "l" or name1[i] == "o" or name1[i] == "v" or name1[i] == "e":
        count2 += 1
        
for i in range(0, len(name2)):
    if name2[i] == "t" or name2[i] == "r" or name2[i] == "u" or name2[i] == "e":
        count1 += 1
    if name2[i] == "l" or name2[i] == "o" or name2[i] == "v" or name2[i] == "e":
        count2 += 1
    
count1 = str(count1)
count2 = str(count2)

final_count = count1 + count2

print(f"Your love match percentage is: {final_count}")
    

