import os
import logging
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime("%Y-%m-%d-%H-%S")}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

LOG_FILE_PATH=os.makedirs(log_path,exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime) ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
if __name__=="__main__":
    logging.info("logging has started")