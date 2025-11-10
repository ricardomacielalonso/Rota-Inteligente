# 🚚 Rota Inteligente: Otimização de Entregas com Algoritmos de IA

**Autor:** Ricardo Maciel Alonso  
**Curso:** Engenharia da Computação – UniFECAF  
**Disciplina:** Artificial Intelligence Fundamentals  

---

## 📌 1. Descrição do Problema e Objetivos

### 🍔 O Desafio “Sabor Express”

A empresa de delivery **Sabor Express** enfrenta um problema crítico: ineficiência logística durante horários de pico.  
As rotas são definidas manualmente, com base apenas na experiência dos entregadores — resultando em **atrasos**, **custos elevados** e **insatisfação dos clientes**.

### 🎯 Objetivos do Projeto

O objetivo principal foi desenvolver uma **Prova de Conceito (PoC)** utilizando **Inteligência Artificial** para otimizar as entregas.

**Objetivos específicos:**
1. Modelar a área de entrega como um **grafo** (locais = nós, ruas = arestas).  
2. Aplicar **clusterização** para dividir os pedidos entre entregadores.  
3. Implementar um algoritmo de **otimização de rotas** (menor caminho).  
4. Criar um **protótipo funcional em Python**, modular e documentado.

---

## 🧭 2. Modelagem do Problema e Representação em Grafo

A cidade é modelada como um **grafo ponderado não direcionado** `G = (V, E)`:

- **Vértices (V):** locais de entrega e o restaurante (ponto inicial).  
- **Arestas (E):** ruas entre locais.  
- **Pesos (W):** custo de deslocamento entre dois pontos.

📏 *Simplificação:* o peso `w(u, v)` foi calculado pela **distância Euclidiana**, adequada para o protótipo.  
Em um sistema real, o peso seria o **tempo de trajeto** (via API de mapas).

📊 Diagrama conceitual disponível em:  
`/outputs/diagrama_grafo_conceitual.png`

---

## 🧩 3. Abordagem da Solução: Estratégia Híbrida

A solução foi dividida em duas fases:

### 🔹 Fase 1: Agrupamento de Entregas com K-Means

**Objetivo:** agrupar pedidos próximos geograficamente para reduzir complexidade.

**Ferramentas:** `scikit-learn`, `matplotlib`.

**Implementação:**
```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
labels = kmeans.fit_predict(coords)
```

📊 Saída visual: `/outputs/clusters_kmeans.png`

⚠️ *Limitação:* o K-Means não garante equilíbrio no número de pedidos por entregador nem otimiza a rota dentro de cada cluster.

---

### 🔹 Fase 2: Otimização de Rota com Algoritmo Genético (TSP)

**Problema:** encontrar a menor rota que visita todos os pontos e retorna ao depósito.  
Esse é o clássico **Problema do Caixeiro Viajante (TSP)** — **NP-difícil**.

#### 💡 Comparação de Abordagens

| Abordagem | Vantagens | Limitações |
|------------|------------|------------|
| A* Search | Boa para caminho único A→B | Escala mal para múltiplos pontos |
| Vizinho Mais Próximo | Rápido e simples | Rota até 25% pior que a ótima |
| **Algoritmo Genético (AG)** | Quase-ótimo e adaptável | Custo computacional moderado |

#### ⚙️ Estrutura do AG (usando `DEAP`)

1. **Indivíduo:** uma permutação de pedidos.  
2. **Fitness:** inverso da distância total.  
3. **Seleção:** torneio.  
4. **Crossover:** `cxOrdered`.  
5. **Mutação:** `mutShuffleIndexes`.  
6. **Parada:** número fixo de gerações ou convergência.

📁 Código principal:  
`src/optimization.py`

---

## 📈 4. Resultados e Eficiência

**Cenário de teste:** 1 entregador, 15 pedidos, 100 gerações.

📉 **Comparação de desempenho:**

| Método | Distância Total (km) | Tempo (s) | Qualidade |
|--------|----------------------|------------|------------|
| Rota Aleatória | ~85.4 | <0.001 | +110% |
| Vizinho Mais Próximo | ~51.2 | 0.005 | +26% |
| **Algoritmo Genético** | **~40.5** | **1.2** | 🔹 Ótima (aproximada) |

**Conclusão:** o AG reduziu a distância em **~21%** comparado ao Vizinho Mais Próximo e **~53%** em relação a uma rota aleatória.

🗺️ Visualização disponível em:  
`/outputs/rota_comparacao_final.png`

---

## 🚧 5. Limitações e Melhorias Futuras

### ⚙️ Limitação 1 – Modelo Estático
O modelo atual é **estático**. Não considera trânsito ou novos pedidos em tempo real.  
➡️ *Melhoria:* adotar um **DVRP (Dynamic Vehicle Routing Problem)** com APIs de tráfego.

### 👨‍🏭 Limitação 2 – Fator Humano
Mudanças tecnológicas enfrentam resistência de motoristas experientes.  
➡️ *Solução:* adicionar **visualizações explicativas** e **feedback via GPS**, como no sistema **UPS ORION**.

### 🚀 Propostas de Evolução
1. **Pesos Dinâmicos:** usar tempo real de APIs (Google Maps, Waze).  
2. **Re-otimização em Tempo Real:** recalcular rotas conforme eventos.  
3. **Aprendizado por Reforço:** futura integração com modelos de *Reinforcement Learning*.

---

## 🧠 6. Conclusão

O projeto demonstrou que é possível **otimizar rotas de entrega com IA**, alcançando:

- Redução de **~20%** no custo de rota.
- Protótipo funcional em **Python**, modular e documentado.
- Base sólida para evolução a um sistema dinâmico inteligente.

Inspirado em soluções de ponta (como o **UPS ORION**), este estudo prova que a **IA clássica e meta-heurísticas** oferecem ganhos reais e mensuráveis para empresas de logística.

---

## 🧰 Tecnologias Utilizadas

| Categoria | Ferramenta |
|------------|-------------|
| Linguagem | Python 3.10 |
| Machine Learning | scikit-learn |
| Otimização Evolutiva | DEAP |
| Visualização | matplotlib |
| Dados | CSV (coordenadas simuladas) |

---

## 🗂️ Estrutura do Projeto

```
📦 Rota-Inteligente
├── data/
│   └── pedidos.csv
├── outputs/
│   ├── clusters_kmeans.png
│   ├── rota_comparacao_final.png
│   └── diagrama_grafo_conceitual.png
├── src/
│   ├── clustering.py
│   └── optimization.py
└── README.md
```

---

## 🧑‍💻 Execução

```bash
# Clonar repositório
git clone https://github.com/ricardomacielalonso/Rota-Inteligente.git
cd rota-inteligente

# Instalar dependências
pip install -r requirements.txt

# Rodar o protótipo
python src/main.py
```

---

## 🧾 Licença

Este projeto foi desenvolvido com fins **acadêmicos** e pode ser livremente adaptado para estudos ou demonstrações técnicas.

---

⭐ **Rota Inteligente — Otimização de Entregas com IA**  
Projeto acadêmico de Engenharia da Computação – UniFECAF.
