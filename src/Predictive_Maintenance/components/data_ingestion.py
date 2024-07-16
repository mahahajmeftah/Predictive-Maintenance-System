import os 
import pandas as pd 
from Predictive_Maintenance import logger
from Predictive_Maintenance.utils.utils import create_directories


from dataclasses import dataclass
@dataclass(frozen=True)
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts")



class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def initiat_data_ingestion(self):
        data = pd.read_csv("notebooks/data/raw.csv")
        logger.info("data read complete")

        create_directories([self.config.raw_data_path])

        data.to_csv(os.path.join(self.config.raw_data_path,"raw.csv"),index=False)
        logger.info("Saved the raw dataset in artifacts directory")


        return self.config.raw_data_path