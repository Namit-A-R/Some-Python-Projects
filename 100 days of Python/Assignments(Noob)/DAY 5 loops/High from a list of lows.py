# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions.
# The highest score in the class is: x

student_scores = input("Enter the scores of students: ").split()
maxi = 0
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
    if student_scores[i] >= maxi:
        maxi = student_scores[i]
        
print(student_scores)
print(f"The heighest score in the class is: {maxi}")