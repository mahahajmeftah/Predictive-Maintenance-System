import pandas as pd 
from src.Predictive_Maintenance import logger
logger.info("welcone_to our project  ")

data = pd.read_csv("/local/home/hadjmefm/Predictive-Maintenance-System/artifacts/transformed_data.csv")
data1 = pd.read_csv("/local/home/hadjmefm/Predictive-Maintenance-System/artifacts/transformed_data1.csv")
data.info()

result = data.compare(data1)
print(result)