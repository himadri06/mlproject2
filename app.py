from src.mlproject2.logger import logging
from src.mlproject2.exception import CustomException
from src.mlproject2.components.data_ingestion import DataIngestionConfig
from src.mlproject2.components.data_ingestion import DataIngestion
from src.mlproject2.components.data_transformation import DataTransformationConfig
from src.mlproject2.components.data_transformation import DataTransformation

import sys

if __name__=='__main__':
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        DataIngestion=DataIngestion()
        train_data_path,test_data_path=DataIngestion.initiate_data_ingestion()
        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    except Exception as e:
        logging.info("Raise Custom Exception")
        raise CustomException(e,sys)