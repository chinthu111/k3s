

import logging
import time
import random

# Configure logging
logging.basicConfig(filename='/var/log/zenoh-app/app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

def generate_log():
    log_level = random.choice(['INFO', 'WARNING', 'ERROR'])
    message = f"This is a {log_level} log message. Random value: {random.randint(1, 100)}"
    if log_level == 'INFO':
        logging.info(message)
    elif log_level == 'WARNING':
        logging.warning(message)
    else:
        logging.error(message)

if __name__ == "__main__":
    while True:
        generate_log()
        time.sleep(random.uniform(1, 5)) # Log every 1 to 5 seconds
