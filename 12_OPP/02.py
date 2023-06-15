import time

def timepassed(current_time):
    def nested():
        time1 = current_time()
        x = input('Dodaj ulubione danie:')
        # time.sleep(2)
        time2 = time.time()
        elapsed_time = time2 - time1
        print(f'Wybrano: {x} trwało to: {elapsed_time} sekundy')
        return time2 - time1
    return nested

@timepassed
def check_time():
    return time.time()

print(check_time())