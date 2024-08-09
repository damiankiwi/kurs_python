from datetime import datetime

def display_friendly_datetime():
    now = datetime.now()

    friendly_str = now.strftime("%A, %B %d, %Y at %I:%M %p")

    print("Current date and time:", friendly_str)

display_friendly_datetime()