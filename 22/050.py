students = [
    {"name": "Alice", "age": 20, "grade": 88},
    {"name": "Bob", "age": 21, "grade": 95},
    {"name": "Charlie", "age": 19, "grade": 72},
    {"name": "David", "age": 22, "grade": 99},
    {"name": "Eva", "age": 20, "grade": 93},
]

high_grade_students = list(filter(lambda student: student['grade'] >= 95, students))

print("Students with grade >= 95:")
for student in high_grade_students:
    print(student)