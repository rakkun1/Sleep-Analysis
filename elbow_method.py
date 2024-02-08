import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def elbow(row, col):
    
    # Loading the data into a DataFrame
    data = pd.read_csv("sleep_data.csv")

    # Extract the relevant columns
    X = data[[row, col]]

    #Normalizing the data
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    wcss = []  # List to store WCSS values

    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        wcss.append(kmeans.inertia_)
    # Plot the elbow curve
    plt.figure(figsize=(8, 4))
    plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
    plt.title('Elbow Method')
    plt.show()

    rate_of_change = [wcss[i] - wcss[i + 1] for i in range(len(wcss) - 1)]
    optimal_clusters = 0
    max_diff = float('-inf')
    for i in range(1, len(rate_of_change)):
        diff = rate_of_change[i - 1] - rate_of_change[i]
        if diff > max_diff:
            max_diff = diff
            optimal_clusters = i + 1

    return optimal_clusters

"""# Loading the data into a DataFrame
data = pd.read_csv("sleep_data.csv")

# Extract the relevant columns
X = data[['Stress Level', 'Quality of Sleep']]

#Normalizing the data
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

wcss = []  # List to store within-cluster sum of squares values

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=89)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

optimal_k = 2 # derived from elbow method

kmeans = KMeans(n_clusters=optimal_k, random_state=89)
clusters = kmeans.fit_predict(X_scaled)

#creating scatter plot to visualise clusters
plt.figure(figsize=(8, 6))
plt.scatter(X['Daily Steps'], X['Quality of Sleep'], c=clusters, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids')
plt.xlabel('Daily Step Count')
plt.ylabel('Quality of Sleep')
plt.legend()
plt.title('K-means Clustering')
plt.show()
"""
