from datetime import datetime, timezone

def generate_rfc3339_timestamp():
    current_time = datetime.now(timezone.utc)

    rfc3339_timestamp = current_time.isoformat()

    return rfc3339_timestamp

print(generate_rfc3339_timestamp())