from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig 
from networksecurity.entity.config_entity import Training_pipeline_config 
import sys

if __name__ == "__main__":
    
    try:
        trainingpipelineconfig =Training_pipeline_config()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()

        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
