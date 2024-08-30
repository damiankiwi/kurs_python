import time

def print_local_time(seconds_since_epoch):
    local_time = time.localtime(seconds_since_epoch)

    print(f"Result: {local_time}")

    print(f"Year: {local_time.tm_year}")


seconds_since_epoch = 414015498
print_local_time(seconds_since_epoch)