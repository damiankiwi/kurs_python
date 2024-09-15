import pendulum

def calculate_age(birthdate_str):
    birthdate = pendulum.parse(birthdate_str)

    today = pendulum.now()

    age = today.diff(birthdate).years

    return age

birthdate = "1990-06-15"
age = calculate_age(birthdate)

print(f"The person is {age} years old.")