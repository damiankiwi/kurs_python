num_students = int(input("Input number of students: "))

students = []

for _ in range(num_students):
    name = input("Name: ")
    grade = float(input("Grade: "))
    students.append([name, grade])

students.sort(key=lambda x: x[1])

second_lowest_grade = None
for i in range(1, num_students):
    if students[i][1] > students[0][1]:
        second_lowest_grade = students[i][1]
        break

names = [student[0] for student in students if student[1] == second_lowest_grade]

print("Names and Grades of all students:")
print(students)

print("Second lowest grade:", second_lowest_grade)

print("Names:")
print("\n".join(names))