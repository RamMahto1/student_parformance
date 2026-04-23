from src.logger import logging
from src.exception import CustomException
import sys
import os
import pickle
from src.utils import load_object
class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            logging.info("prediction has been started")
            # Load the model and preprocessor
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            
            model = self.load_object(model_path)
            preprocessor = self.load_object(preprocessor_path)
            
            # Preprocess the input features
            data_scaled = preprocessor.transform([features])
            
            # Make prediction
            prediction = model.predict(data_scaled)
            
            logging.info("prediction has been completed")
            return prediction
        
        except Exception as e:
            logging.error("an error has occurred during prediction")
            raise CustomException(e, sys)
    
    def load_object(self, file_path):
        """
        Load a pickle object from file
        """
        try:
            with open(file_path, 'rb') as file_obj:
                return pickle.load(file_obj)
        except Exception as e:
            raise CustomException(e, sys)
   