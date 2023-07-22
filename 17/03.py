import datetime

def get_current_date_time():
    current_date_time = datetime.datetime.now()
    return current_date_time.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    current_date_time_str = get_current_date_time()
    print("Current date and time:")
    print(current_date_time_str)