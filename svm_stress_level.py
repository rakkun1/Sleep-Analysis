
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("sleep_data.csv")

# Select relevant features for clustering (quality of sleep and physical activity)
features = data[['Stress Level', 'Sleep Duration']]

# Preprocess and scale the features (if needed)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


wcss = []
max_k = 10 

for k in range(1, max_k + 1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)

"""# Plot the elbow curve
plt.plot(range(1, max_k + 1), wcss, marker='o')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.title('Elbow Method')
plt.show()"""

# Choose an appropriate value for K based on the elbow plot (the "elbow" point)

chosen_k = 2
kmeans = KMeans(n_clusters=chosen_k, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

# Add cluster labels to the original dataset
data['cluster_label'] = clusters

# Visualize the clusters
plt.scatter(data['Stress Level'], data['Sleep Duration'], c=clusters, cmap='viridis')
plt.xlabel('Stress Level')
plt.ylabel('Sleep Duration')
plt.title('K-means Clustering')
plt.show()
