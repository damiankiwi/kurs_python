import pendulum

def time_until_event(event_datetime):
    current_datetime = pendulum.now()

    time_until_event = current_datetime.diff(event_datetime)

    print(f"Time remaining until the event ({event_datetime.format('YYYY-MM-DD HH:mm:ss')}): {time_until_event.in_words()}")

future_event_str = "2023-12-31 18:00:00"

future_event_datetime = pendulum.parse(future_event_str)

time_until_event(future_event_datetime)