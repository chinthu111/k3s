import logging
import time
import random

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Dummy log generator
def generate_logs():
    while True:
        log_level = random.choice(["INFO", "WARNING", "ERROR"])
        message = f"This is a {log_level} log message."
        
        if log_level == "INFO":
            logger.info(message)
        elif log_level == "WARNING":
            logger.warning(message)
        elif log_level == "ERROR":
            logger.error(message)
        
        time.sleep(random.randint(1, 5))

if __name__ == "__main__":
    generate_logs()