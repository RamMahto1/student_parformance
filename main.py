from src.logger import logging
from src.exception import CustomException
import sys
import os

logging.info("main.py has been started")

try:
    a=10
    b=20
    c=a/b
    logging.info(f"the value of c is {c}")
except Exception as e:
    logging.error("an error has occured in main.py")
    raise CustomException(e,sys)

