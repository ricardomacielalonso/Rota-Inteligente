import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def agrupar_pedidos(csv_path, n_clusters=3, output_path="outputs/clusters_kmeans.png"):
    df = pd.read_csv(csv_path)
    coords = df[['latitude', 'longitude']].values

    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', n_init=10, random_state=42)
    df['cluster'] = kmeans.fit_predict(coords)

    plt.figure(figsize=(6,6))
    plt.scatter(df['latitude'], df['longitude'], c=df['cluster'], cmap='viridis')
    plt.title('Clusterização de Pedidos (K-Means)')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.savefig(output_path)
    plt.close()

    return df, kmeans.cluster_centers_
