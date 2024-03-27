import datetime


class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        current_date = datetime.date.today()
        age = current_date.year - self.dob.year - (
                    (current_date.month, current_date.day) < (self.dob.month, self.dob.day))
        return age


def get_date_of_birth():
    while True:
        dob_str = input("Enter person's date of birth (YYYY-MM-DD): ")
        try:
            dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()
            return dob
        except ValueError:
            print("Error: Invalid date format. Please enter the date in YYYY-MM-DD format.")


name = input("Enter person's name: ")
country = input("Enter person's country: ")
dob = get_date_of_birth()

person = Person(name, country, dob)
age = person.calculate_age()
print(f"{person.name} from {person.country} is {age} years old.")