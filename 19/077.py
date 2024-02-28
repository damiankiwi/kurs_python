def gpa_to_letter_grade(gpa):
    if gpa == 4.0:
        return 'A+'
    elif gpa >= 3.7:
        return 'A'
    elif gpa >= 3.4:
        return 'A-'
    elif gpa >= 3.0:
        return 'B+'
    elif gpa >= 2.7:
        return 'B'
    elif gpa >= 2.4:
        return 'B-'
    elif gpa >= 2.0:
        return 'C+'
    elif gpa >= 1.7:
        return 'C'
    elif gpa >= 1.4:
        return 'C-'
    else:
        return 'F'

def convert_gpas_to_letter_grades(gpas):
    return [gpa_to_letter_grade(gpa) for gpa in gpas]

input1 = [4.0, 3.5, 3.8]
output1 = convert_gpas_to_letter_grades(input1)

input2 = [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
output2 = convert_gpas_to_letter_grades(input2)

print(f"Input 1: {input1}")
print(f"Output 1: {output1}")

print(f"Input 2: {input2}")
print(f"Output 2: {output2}")