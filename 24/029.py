 # Import the Pendulum module
import pendulum

def calculate_age_in_weeks(birthdate):
    current_date = pendulum.now()

    birthdate = pendulum.parse(birthdate)

    age_in_weeks = current_date.diff(birthdate).in_weeks()

    return age_in_weeks

birthdate_str = "1990-05-15"

person_age_in_weeks = calculate_age_in_weeks(birthdate_str)

print(f"The person's age in weeks with birthdate {birthdate_str} is approximately {person_age_in_weeks} weeks.")