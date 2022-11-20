import random

names = ["Nandu", "Namit", "Salu", "Namita", "Tittu"]
students_marks = {student: random.randint(1, 100) for student in names}
print(students_marks)
passed_students = {student: score for (student, score) in students_marks.items() if score > 45}
print(passed_students)
