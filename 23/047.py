import calendar

def get_second_saturdays(year):
    second_saturdays = []

    for month in range(1, 13):
        month_cal = calendar.monthcalendar(year, month)

        first_week = month_cal[0]
        second_week = month_cal[1]

        if first_week[calendar.SATURDAY] != 0:
            second_saturday = second_week[calendar.SATURDAY]
        else:
            third_week = month_cal[2]
            second_saturday = third_week[calendar.SATURDAY]

        second_saturdays.append(f'{year}-{month:02d}-{second_saturday:02d}')

    return second_saturdays

year = 2024
second_saturdays = get_second_saturdays(year)
for date in second_saturdays:
    print(date)