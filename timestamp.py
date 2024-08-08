from datetime import datetime
import time


def timestamps():
    timestamp_ms = time.time()
    timestamp = int(timestamp_ms * 1000)
    dt_object = datetime.fromtimestamp(timestamp_ms)
    formatted_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")
    return timestamp, formatted_time


if __name__ == "__main__":
    t = timestamps()
    print(t)
