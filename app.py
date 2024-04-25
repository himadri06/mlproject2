from src.mlproject2.logger import logging
from src.mlproject2.exception import CustomException
from src.mlproject2.components.data_ingestion import DataIngestionConfig
from src.mlproject2.components.data_ingestion import DataIngestion

import sys

if __name__=='__main__':
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        DataIngestion=DataIngestion()
        DataIngestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Raise Custom Exception")
        raise CustomException(e,sys)