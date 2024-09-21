# Import the Pendulum module
import pendulum

def calculate_business_days(start_date, end_date):
    business_days = 0

    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:
            business_days += 1

        current_date = current_date.add(days=1)

    return business_days

start_date_str = "2020-12-01"
end_date_str = "2020-12-31"

start_date = pendulum.parse(start_date_str)
end_date = pendulum.parse(end_date_str)

business_days = calculate_business_days(start_date, end_date)

print(f"Business days between {start_date_str} and {end_date_str}: {business_days} days")