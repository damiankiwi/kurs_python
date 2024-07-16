from datetime import datetime

date_string = "Jul 1 2014 2:43PM"

date_time_obj = datetime.strptime(date_string, '%b %d %Y %I:%M%p')

print(date_time_obj)