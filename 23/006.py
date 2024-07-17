from datetime import datetime

unix_timestamp = 1284105682

readable_date = datetime.fromtimestamp(unix_timestamp)

print(f"Readable date : {readable_date}")