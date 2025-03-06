import time
import random

from otel_instrumentation import configure_otel

counter, logger = configure_otel()

def generate_logs():
    levels = ["INFO", "WARNING", "ERROR"]
    messages = [
        "Application started successfully.",
        "Processing data...",
        "Network connection lost.",
        "Database query failed.",
        "User login successful.",
        "File not found.",
    ]

    level = random.choice(levels)
    message = random.choice(messages)
    counter.add(1)
    if level == "INFO":
        logger.info(message)
    elif level == "WARNING":
        logger.warning(message)
    else:
        logger.error(message)

if __name__ == "__main__":
    while True:
        generate_logs()
        time.sleep(random.uniform(1, 5))
