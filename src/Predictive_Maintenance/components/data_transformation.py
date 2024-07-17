import os 
from pathlib import Path
import pandas as pd 
import numpy as np 
import pickle
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
from Predictive_Maintenance import logger
from Predictive_Maintenance.utils.utils import create_directories,type_of_failure


from dataclasses import dataclass
@dataclass(frozen=True)
class DataTransformationConfig:
    transormed_data_path:str = os.path.join("artifacts")



class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config

    def initiate_data_transformation(self):
        data = pd.read_csv("artifacts/raw.csv")
        logger.info("data read complete")

        data.drop(['UDI', 'Product ID'], axis=1, inplace=True)
        logger.info("dropping UDi,ProductId")


        #categorical encoding
        encoder = OrdinalEncoder(categories=[['L', 'M', 'H']])
        data['Type'] = encoder.fit_transform(data[['Type']])
        logger.info("categorical encoding for Type column")

        #creating type of failure column
        data.apply(lambda row :type_of_failure(row.name,data),axis=1)
        data['type_of_failure'].replace(np.NaN, 'no failure', inplace=True)
        data.drop(['TWF', 'HDF', 'PWF', 'OSF', 'RNF'], axis=1, inplace=True)


        #label encoding for the type of failure column
        encoder = LabelEncoder()
        data['type_of_failure'] = encoder.fit_transform(data['type_of_failure'])
        logger.info("lablel encoding for type_of_failure column")
        
        #converting temperature from Kalvin to Celcius
        data['Air temperature [c]'] = data['Air temperature [K]'] - 273.15
        data['Process temperature [c]'] = data['Process temperature [K]'] - 273.15
        data.drop(['Air temperature [K]', 'Process temperature [K]'], axis=1, inplace=True)
        logger.info("converting temperature from Kalvin to Celcius")



        #feature Scaling
        scaler = MinMaxScaler()
        scale_cols = ['Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Air temperature [c]', 'Process temperature [c]']
        data_scaled = scaler.fit_transform(data[scale_cols])
        with open(Path("artifacts", "scaler.pkl"), "wb") as f:
                pickle.dump(scaler, f) 
        logger.info("saving the scaler in the artifact dir")

        data_scaled = pd.DataFrame(data_scaled)
        data_scaled.columns = scale_cols
        data.drop(scale_cols, axis=1, inplace=True)
        data_scaled = pd.concat([data, data_scaled], axis=1)
        logger.info("Feature scaling completed successfully")

        #oversampling
        smote = SMOTE(sampling_strategy='auto',random_state=42)
        X = data_scaled.drop('type_of_failure', axis=1)
        y = data_scaled['type_of_failure']
        X_resampled, y_resampled = smote.fit_resample(X, y)
        df_sampled = pd.concat([X_resampled, y_resampled], axis=1)
        logger.info("Oversampling completed successfully")
        


        df_sampled.to_csv(os.path.join(self.config.transormed_data_path,"transformed_data.csv"),index=False)
        logger.info("Saved the transformed dataset in artifacts directory")


        return df_sampled