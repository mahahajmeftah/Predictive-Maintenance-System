## Predictive-Maintenance-System
<p>
<a href="#problem">Problem Statement</a> •
<a href="#system">System Description</a> •
<a href ="#dataset">Dataset<a> •
<a href ="#pipeline">Pipeline<a> •
</p>

[Screencast from 08-21-2024 08:59:25 AM.webm](https://github.com/user-attachments/assets/3374bedb-838d-4dd4-82ae-c73f2e5e1f1c)
<a id='porblem'></a>
## Problem Statement
- Build an end-to-end machine learning system that predicts wether a particular equipement will fail or not. The features include air, process temperatures, rotational speed, troque and tool wear.

- It should be a fault-tolerant, monitored, and containerized web service that recieves the object's features and returns wether the equipement will fail.
<a id='system'></a>
## System Description
The system contains the following parts:
- Experiment tracking and model registry with `MLFlow`
- Web Service Deployment wiht `Flask`
- `Docker` Containerizaton
- Cloud Hosting with `AWS EC2`
- Model Monitoring with `Evidently AI`
- CI/CD with `Github Actions`

<a id='dataset'></a>
## Dataset
The dataset consists of more than 50,000 data points. It contains 14 features and the target column `Machine Failure`
<a id='pipeline'></a>
## Pipeline
1. **Input Data**
   - Source: CSV file

2. **Preprocessing**
   - Clean, transform, and prepare data
   - Tasks: Missing value imputation, feature scaling, categorical variable encoding

3. **Model Training**
   - Train machine learning models
   - Supports multiple models for experimentation and comparison

4. **Model Evaluation**
   - Evaluate trained models using appropriate metrics(`ROC_AUC,Accuracy`)
   - Select the best-performing model for deployment

5. **Docker Container**
   - Package application code, model artifacts, frontend, and backend components
   - Ensures consistent deployment across environments

6. **AWS EC2**
   - Deploy Docker container with dependencies on AWS EC2
   - Provides scalability, reliability, and easy management

7. **Web App Flask**
   - Accessible via web browser
   - User-friendly interface for interacting with prediction functionality

8. **Prediction**
   - Generate predictions using input data from the web application
   - Display predictions to the user via the web interface

9. **CI/CD Pipeline**
    - Automated using GitHub Actions
    - Ensures continuous integration and deployment
    - Provides a consistent experience for users

