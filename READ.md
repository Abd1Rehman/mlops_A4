# MLOps Pipeline Assignment  

**Student Name:** Abdul Rehamn 
**Student ID:** 22I-0616 

## Project Overview  
This project demonstrates a complete **MLOps pipeline** for a simple machine learning task using the **Boston Housing dataset**. The pipeline includes **data versioning, preprocessing, model training, evaluation, and experiment tracking** using **DVC, MLflow, Python, and Jenkins/GitHub Workflows**.  

The goal is to implement an end-to-end workflow for reproducible and automated machine learning operations.

## Project Structure
mlops-mlflow-assignment/
│
├─ data/ # Raw and processed datasets
├─ src/ # Python scripts
│ ├─ pipeline_components.py # ML pipeline functions
│ ├─ model_training.py # Model training script
├─ components/ # Compiled MLflow components (if applicable)
├─ pipeline.py # Main pipeline orchestration with MLflow
├─ requirements.txt # Project dependencies
├─ Dockerfile # Custom image for pipeline execution
├─ Jenkinsfile # Jenkins pipeline automation
├─ .dvc/ # DVC configuration
└─ README.md # Project documentation

bash
Copy code

## Setup Instructions
1. **Clone the repository**  
```bash
git clone <repository-url>
cd mlops-mlflow-assignment
Install dependencies

bash
Copy code
pip install -r requirements.txt
DVC setup

bash
Copy code
dvc init
dvc remote add -d myremote <remote-url>
dvc pull
MLflow tracking

bash
Copy code
mlflow ui
All experiments, model versions, and metrics are tracked in MLflow.

Running the Pipeline
Run the main pipeline:

bash
Copy code
python pipeline.py
MLflow will track the following stages:

Data extraction from DVC

Data preprocessing

Model training

Model evaluation

Check the MLflow UI to view model metrics, parameters, and artifacts.

Continuous Integration
The Jenkinsfile/GitHub Workflow automates the pipeline:

Environment setup (install dependencies)

Pipeline compilation and testing

Optional: automatic MLflow experiment logging

Notes
Dataset used: Boston Housing

Model: Random Forest Regressor

Metrics logged: RMSE, R², MAE

Repository Link
[Insert your GitHub repository URL here]
