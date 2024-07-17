from Predictive_Maintenance.components.data_transformation import DataTransformationConfig,DataTransformation
try:
    transformation_config = DataTransformationConfig()
    data_transformation = DataTransformation(transformation_config)
    df_transformed = data_transformation.initiate_data_transformation()
except Exception as e:
    raise e