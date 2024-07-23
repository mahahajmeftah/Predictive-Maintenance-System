import pandas as pd 
from src.Predictive_Maintenance import logger
from Predictive_Maintenance.pipelines.prediction import Prediction
logger.info("welcone_to our project  ")

type_value= "Low"
rpm =1412
torque = 52.3
tool_wear = 218
air_temp = 25.15
process_temp = 34.95

predictor = Prediction()
result = predictor.predict(type_value,rpm,torque,tool_wear,air_temp,process_temp)
print(result)