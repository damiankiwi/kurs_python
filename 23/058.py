import time

def sleep_and_print(seconds, repeat):
    for _ in range(repeat):
        print(f"Sorry, Slept for {seconds} seconds...")
        time.sleep(seconds)

sleep_and_print(3, 4)