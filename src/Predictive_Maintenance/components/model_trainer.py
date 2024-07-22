import os 
import pandas as pd 
import pickle
from sklearn.ensemble import RandomForestClassifier
from dataclasses import dataclass
from Predictive_Maintenance import logger


@dataclass
class ModelTrianerConfig:
    model_path:str = os.path.join("artifacts","model.pkl")
    data_train_path : str = os.path.join("artifacts","train.csv")
    data_test_path : str = os.path.join("artifacts","test.csv")


class ModelTrainer:
    def __init__(self,config:ModelTrianerConfig):
        self.config = config

    def train(self):
        train = pd.read_csv(self.config.data_train_path)
        test = pd.read_csv(self.config.data_test_path)
        logger.info("train and test loaded")
        x_train = train.drop(["Machine failure","type_of_failure"],axis=1)
        y_train = train["Machine failure"]
        x_test = test.drop(["Machine failure","type_of_failure"],axis=1)
        y_test = test["Machine failure"]

        best_params = {
        'max_depth': 15,
        'min_samples_leaf': 1,
        'min_samples_split': 2,
        'n_estimators': 50
        }

        #Model with the best parameters
        model = RandomForestClassifier(
            max_depth=best_params['max_depth'],
            min_samples_leaf=best_params['min_samples_leaf'],
            min_samples_split=best_params['min_samples_split'],
            n_estimators=best_params['n_estimators'],
            random_state=42
        )

        # Train the model
        model.fit(x_train, y_train)

        with open(self.config.model_path, 'wb') as f:
                pickle.dump(model, f) 

       

        
