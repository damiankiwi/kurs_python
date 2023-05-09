grades = {}.fromkeys(['Math', 'English', 'Art'], 3)
print(grades)

print(grades.keys())
print(list(sorted(grades.keys())))
print(tuple(sorted(grades.keys())))
print(set(sorted(grades.keys())))