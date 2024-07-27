import datetime

def drop_microseconds(dt):
    return dt.replace(microsecond=0)

sample_datetime = datetime.datetime.now()

print("Original datetime with microseconds:", sample_datetime)

updated_datetime = drop_microseconds(sample_datetime)
print("Datetime without microseconds:", updated_datetime)