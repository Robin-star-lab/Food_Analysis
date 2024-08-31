import os
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split




@dataclass
class data_ingestion_config:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')
    
class data_ingestion:
    def __init__(self):
        self.data_ingestion_config=data_ingestion_config()
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df =pd.read_csv('food_data.csv')
            logging.info("Entered the dataset as csv file")
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Initiate train test split")
            train_set,test_set=train_test_split(df,test_size=0.25,random_state=30)
            
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("indestion of data completed")
            
            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=data_ingestion()
    obj.initiate_data_ingestion()