from Predictive_Maintenance.components.model_trainer import ModelTrianerConfig,ModelTrainer
try:
    model_trainer_config = ModelTrianerConfig()
    model_trainer = ModelTrainer(model_trainer_config)
    df_transformed = model_trainer.train()
except Exception as e:
    raise e




