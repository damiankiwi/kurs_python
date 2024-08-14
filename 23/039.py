from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()

    age = today.year - birthdate.year

    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1

    return age

birthdate = datetime(1990, 8, 9)
age = calculate_age(birthdate)

print(f"Age: {age} years")