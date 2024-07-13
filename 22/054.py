from datetime import datetime

def filter_future_dates(dates):

    current_date = datetime.now().date()
    return list(filter(lambda date: datetime.strptime(date, "%Y-%m-%d").date() <= current_date, dates))

dates = ["2024-05-26", "2023-01-01", "2022-12-31", "2023-12-31", "2024-01-01"]

filtered_dates = filter_future_dates(dates)

print("Dates that are not in the future:")
print(filtered_dates)