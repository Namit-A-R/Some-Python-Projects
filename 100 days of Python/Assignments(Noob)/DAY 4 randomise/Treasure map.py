#Dont change the code below
row1 = ["#", "#", "#"]
row2 = ["#", "#", "#"]
row3 = ["#", "#", "#"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
#write your code below
position = input("Where do you want to put the treasure?: ")
x = int(position[0]) - 1
y = int(position[1]) - 1
map[y][x] = "T"
print(f"{row1}\n{row2}\n{row3}\n")

