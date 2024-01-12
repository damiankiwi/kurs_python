def usun_samogloski(ciag):
    samogloski = "aeiouAEIOU"
    return ''.join(char for char in ciag if char not in samogloski)

print("Oryginalny ciąg: Python")
print("Po usunięciu wszystkich samogłosek:", usun_samogloski("Python"))

print("Oryginalny ciąg: C Sharp")
print("Po usunięciu wszystkich samogłosek:", usun_samogloski("C Sharp"))

print("Oryginalny ciąg: JavaScript")
print("Po usunięciu wszystkich samogłosek:", usun_samogloski("JavaScript"))