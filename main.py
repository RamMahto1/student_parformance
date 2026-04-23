from src.logger import logging
from src.exception import CustomException
import sys
import os
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.utils import save_object
from src.components.data_validation import DataValidation

from src.components.model_trainer import ModelTrainer
from src.pipeline.predict_pipeline import PredictPipeline


## 1: Data Ingestion 
data_ingestion=DataIngestion()
train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
logging.info("data ingestion has been completed")
# logging.info("main.py has been started")

# 2: Data Transformation
data_transformation = DataTransformation()
train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
logging.info("data transformation has been completed")

# 3: Data Validation
data_validation = DataValidation()
data_validation.validate_data(train_data_path, test_data_path)
logging.info("data validation has been completed")

# 4: Model Training
model_trainer = ModelTrainer()
report,best_model_name,best_model,best_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
logging.info(f"Best Model: {best_model_name} with score: {best_score}")

# 5: prediction pipeline
predict_pipeline = PredictPipeline()
prediction = predict_pipeline.predict(test_arr[0][:-1])
logging.info(f"Prediction for first test sample: {prediction}")

# try:
#     a=10
#     b=20
#     c=a/b
#     logging.info(f"the value of c is {c}")
# except Exception as e:
#     logging.error("an error has occured in main.py")
#     raise CustomException(e,sys)

