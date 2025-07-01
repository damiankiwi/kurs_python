from collections import namedtuple

Employee = namedtuple("Employee", ["name", "age", "country"])

def main():
    try:
        employees = [
            Employee("Klaes Susana", 35, "USA"),
            Employee("Auxentius Cloe", 44, "Canada"),
            Employee("Golzar Merob", 28, "UK"),
            Employee("Tatjana Adhelm", 30, "Australia"),
        ]

        for employee in employees:
            print("Employee Name:", employee.name)
            print("Employee Country:", employee.country)
            print()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()