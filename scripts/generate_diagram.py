# scripts/generate_diagram.py
import networkx as nx
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

# Exemplo conceitual: nó 0 = restaurante, 1..4 = clientes
G = nx.Graph()
edges = [
    (0,1), (0,2), (0,3), (0,4),
    (1,2), (2,3), (3,4)
]
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)  # layout bonito e reproduzível
plt.figure(figsize=(6,6))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=600)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=12)
plt.title("Diagrama Conceitual do Grafo (Cidade / Entregas)")
plt.axis('off')
plt.tight_layout()
plt.savefig("outputs/diagrama_grafo_conceitual.png", dpi=150)
plt.close()

print("Gerado: outputs/diagrama_grafo_conceitual.png")