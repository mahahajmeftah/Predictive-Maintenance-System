from Predictive_Maintenance.components.data_ingestion import DataIngestionConfig ,DataIngestion
try:
    ingestion_config = DataIngestionConfig()
    data_ingestion = DataIngestion(ingestion_config)
    raw_data_path = data_ingestion.initiat_data_ingestion()
except Exception as e:
    raise e




