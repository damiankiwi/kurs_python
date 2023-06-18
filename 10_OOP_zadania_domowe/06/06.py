class Employee:
    def __init__(self, name, surname, position, salary, student_status):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.student_status = student_status

    def calculate_raise(self):
        raise_percentage = 0.05
        self.salary += self.salary * raise_percentage

    def calculate_tax(self):
        tax_rate = 0.2
        minimum_health_contribution = 100
        earnings = self.salary - minimum_health_contribution

        if self.student_status:
            return 0
        else:
            tax_amount = earnings * tax_rate
            return tax_amount

    def generate_email(self, company_name):
        email = ""
        consonants = "bcdfghjklmnpqrstvwxyz"

        for char in (self.name + self.surname):
            if char.lower() in consonants:
                email += char.lower()

        email += "@" + company_name.lower() + ".com"
        email = email.replace(" ", "")
        return email


if __name__ == "__main__":
    company_name = "Love Python Company"

    adam = Employee("Adam", "Kowalski", "Python", 10000, False)
    bogdan = Employee("Bogdan", "Nowak", "Tester", 3000, True)

    adam.calculate_raise()
    adam_tax = adam.calculate_tax()
    adam_email = adam.generate_email(company_name)

    bogdan.calculate_raise()
    bogdan_tax = bogdan.calculate_tax()
    bogdan_email = bogdan.generate_email(company_name)

    print("Salary after raise:", adam.salary)
    print("Tax amount:", adam_tax)
    print("Email:", adam_email)
    print('--------------------------------')
    print("Salary after raise:", bogdan.salary)
    print("Tax amount:", bogdan_tax)
    print("Email:", bogdan_email)