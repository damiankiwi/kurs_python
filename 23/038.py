import os
import datetime


def get_last_modified_time(file_path):
    timestamp = os.path.getmtime(file_path)

    last_modified_time = datetime.datetime.fromtimestamp(timestamp)

    return last_modified_time


file_path = 'example.txt'
last_modified_time = get_last_modified_time(file_path)

print(f"The file '{file_path}' was last modified on: {last_modified_time}")