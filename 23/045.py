import datetime

def get_current_week():
    current_date = datetime.date.today()

    week_number = current_date.isocalendar()[1]

    return week_number

current_week = get_current_week()
print(f"Current Week Number: {current_week}")