from src.logger import logging
from src.exception import CustomException
import sys
import os
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.utils import save_object


## 1: Data Ingestion 
data_ingestion=DataIngestion()
train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
logging.info("data ingestion has been completed")
# logging.info("main.py has been started")

# 2: Data Transformation
data_transformation = DataTransformation()
preprocessor_obj, train_arr, test_arr = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
logging.info("data transformation has been completed")

# try:
#     a=10
#     b=20
#     c=a/b
#     logging.info(f"the value of c is {c}")
# except Exception as e:
#     logging.error("an error has occured in main.py")
#     raise CustomException(e,sys)

