file1 = open('file1.txt').readlines()
file2 = open('file2.txt').readlines()

common_elements = [int(number) for number in file1 if number in file2]

print(common_elements)
# print(result)
