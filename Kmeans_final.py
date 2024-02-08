from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

# Assuming 'data' is your dataset containing 'Daily Steps' and 'Age'
# Replace this with your actual data

# Step 2: Prepare Data
# Assume 'data' contains 'Daily Steps' and 'Age' columns
data = pd.read_csv("sleep_data.csv")
X = data[['Physical Activity Level', 'Stress Level']].values

# Step 3: Choose Number of Clusters (K)
# Choose an appropriate number of clusters (K) based on your analysis or using techniques like the Elbow Method
n_clusters = 3  # Example: selecting 3 clusters

# Step 4: Fit K-means Model
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)

# Step 5: Obtain Cluster Labels
cluster_labels = kmeans.labels_
data['Cluster'] = cluster_labels

# Step 6: Visualize Clusters
plt.scatter(data['Daily Steps'], data['Age'], c=data['Cluster'], cmap='viridis', s=50)
plt.xlabel('Daily Steps')
plt.ylabel('Age')
plt.title('K-means Clustering')
plt.show()