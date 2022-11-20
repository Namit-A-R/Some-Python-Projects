# you are going to write a programme that calculates the average height os the students
# from a list of heights,
# the avg height can be calculated by adding all the heights and dividing by the total
# number of students

student_height = input("Input a list of student heights: ")
student_height = student_height.split()
no_of_students = len(student_height)
sum_of_heights = 0
for i in range(0, no_of_students):
    student_height[i] = int(student_height[i])
    sum_of_heights += student_height[i]

average_height = sum_of_heights / no_of_students
print(f"The average height of {no_of_students} students is: {average_height}")
