from datetime import datetime, timedelta

def get_dates_between(start_date, end_date):
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    date_list = []

    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)

    return date_list

start_date = "2023-08-01"
end_date = "2023-08-05"

dates = get_dates_between(start_date, end_date)

for date in dates:
    print(date.strftime("%Y-%m-%d"))