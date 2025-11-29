MLOps Pipeline Assignment

Student Name: [Your Name]
Student ID: [Your ID]

Project Overview

This project demonstrates a complete MLOps pipeline for a simple machine learning task (Boston Housing dataset). The pipeline covers data versioning, preprocessing, model training, evaluation, and experiment tracking using industry-standard tools: DVC, MLflow, Python, and Jenkins/GitHub Workflows.

The objective is to implement an end-to-end workflow for reproducible and automated machine learning operations.

Project Structure
mlops-mlflow-assignment/
│
├─ data/                   # Raw and processed datasets
├─ src/                    # Python scripts
│   ├─ pipeline_components.py  # ML pipeline functions
│   ├─ model_training.py       # Model training script
├─ components/             # Compiled MLflow components (if applicable)
├─ pipeline.py             # Main pipeline orchestration with MLflow
├─ requirements.txt        # Project dependencies
├─ Dockerfile              # Custom image for pipeline execution
├─ Jenkinsfile             # Jenkins pipeline automation
├─ .dvc/                   # DVC configuration
└─ README.md               # Project documentation

Setup Instructions

Clone the repository:

git clone <repository-url>
cd mlops-mlflow-assignment


Install dependencies:

pip install -r requirements.txt


DVC setup:

Initialize DVC: dvc init

Configure remote storage: dvc remote add -d myremote <remote-url>

Pull data: dvc pull

MLflow tracking:

Start MLflow server locally:

mlflow ui


All experiments, model versions, and metrics are logged in MLflow.

Running the Pipeline

Execute the main pipeline:

python pipeline.py


MLflow will track the following stages:

Data extraction from DVC

Data preprocessing

Model training

Model evaluation

Check MLflow UI for model metrics, parameters, and artifacts.

Continuous Integration

The Jenkinsfile/GitHub Workflow automates the pipeline:

Environment setup (install dependencies)

Pipeline compilation and test

Optional: automatic MLflow experiment logging

Notes

Dataset used: Boston Housing

Model: Random Forest Regressor

Metrics logged: RMSE, R², MAE

Repository Link

[Insert your GitHub repository URL here]
