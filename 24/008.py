import pendulum

datetime_string = "2019-02-01 15:45:00"

parsed_time = pendulum.parse(datetime_string)

print(f"Parsed Pendulum object: {parsed_time}")