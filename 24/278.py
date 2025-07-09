from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "marks"])

def calculate_average_grade(student):
    total_marks = sum(student.marks)
    average_grade = total_marks / len(student.marks)
    return average_grade

student1 = Student(name="Ain Ruth", age=22, marks=[89, 92, 75, 90, 86])

average_grade = calculate_average_grade(student1)
print("Average Grade:", average_grade)