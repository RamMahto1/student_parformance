#from src.logger import logging
from src.exception import CustomException
import sys
import os
import pandas as pd
from src.logger import logging


class DataValidation:
    def __init__(self):
        pass
    
    def validate_data(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            # Basic checks
            if train_df.shape[0] == 0:
                raise Exception("Train dataset is empty")
            if test_df.shape[0] == 0:
                raise Exception("Test dataset is empty")
            
            #  Data Details Logging
            logging.info(f"Train shape: {train_df.shape}")
            logging.info(f"Test shape: {test_df.shape}")
            
            logging.info(f"Train columns: {train_df.columns.tolist()}")
            logging.info(f"Test columns: {test_df.columns.tolist()}")
            
            logging.info(f"Train dtypes:\n{train_df.dtypes}")
            logging.info(f"Test dtypes:\n{test_df.dtypes}")
            
            # Missing values
            logging.info(f"Train missing values:\n{train_df.isnull().sum()}")
            logging.info(f"Test missing values:\n{test_df.isnull().sum()}")
            
            # Duplicate check
            logging.info(f"Train duplicates: {train_df.duplicated().sum()}")
            logging.info(f"Test duplicates: {test_df.duplicated().sum()}")
            
            #  describe (numerical summary)
            logging.info(f"Train describe:\n{train_df.describe()}")
            
            logging.info("Data validation completed successfully")
        
        except Exception as e:
            raise CustomException(e, sys)