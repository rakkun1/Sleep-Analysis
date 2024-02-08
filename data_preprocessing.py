import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Loading the data into a DataFrame
data = pd.read_csv("sleep_data.csv")

#print(data.head())

# Replace missing values in numerical features with the mean
data['Sleep Duration'].fillna(data['Sleep Duration'].mean(), inplace=True)

# Replace missing values in categorical features with the mode
data['BMI Category'].fillna(data['BMI Category'].mode()[0], inplace=True)

# Convert categorical variables to one-hot encoding
data = pd.get_dummies(data, columns=['Occupation', 'BMI Category'], drop_first=True)

from sklearn.preprocessing import StandardScaler

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the numerical features
data[['Sleep Duration', 'Stress Level', 'Daily Steps']] = scaler.fit_transform(data[['Sleep Duration', 'Stress Level', 'Daily Steps']])

print(data.head())
