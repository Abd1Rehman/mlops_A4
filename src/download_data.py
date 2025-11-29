# src/download_data.py

from sklearn.datasets import fetch_california_housing
import pandas as pd

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame  # this gives a pandas DataFrame with features + target

# Save raw data
df.to_csv("data/raw_data.csv", index=False)
print("Dataset saved to data/raw_data.csv")
