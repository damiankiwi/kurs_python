import time

epoch = time.gmtime(0)
print("Epoch on a given platform:")
print(epoch)

seconds_since_epoch = 36000
converted_time = time.gmtime(seconds_since_epoch)
print("\nTime in seconds since the epoch:")
print(converted_time)