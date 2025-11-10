from src.clusterization import agrupar_pedidos
from src.optimization import otimizar_rota
import pandas as pd
import matplotlib.pyplot as plt

# 1. Clusterização
df, centros = agrupar_pedidos("data/pedidos.csv", n_clusters=3)

# 2. Escolhe um cluster para otimizar a rota
cluster_id = 0
pontos = df[df['cluster'] == cluster_id][['latitude', 'longitude']].values.tolist()

# 3. Otimização com Algoritmo Genético
melhor_rota, distancia = otimizar_rota(pontos, n_geracoes=100)
print(f"Melhor rota (cluster {cluster_id}): {melhor_rota}")
print(f"Distância total: {distancia:.2f}")

# 4. Visualização
rota_coords = [pontos[i] for i in melhor_rota] + [pontos[melhor_rota[0]]]
x, y = zip(*rota_coords)
plt.plot(x, y, marker='o')
plt.title(f'Rota Otimizada - Cluster {cluster_id}')
plt.savefig("outputs/rota_comparacao_final.png")
plt.close()
