import random
import numpy as np
from deap import base, creator, tools, algorithms

def calcular_distancia(pontos, rota):
    dist = 0
    for i in range(len(rota)):
        a, b = pontos[rota[i]], pontos[(i+1) % len(rota)]
        dist += np.linalg.norm(np.array(a) - np.array(b))
    return dist

def otimizar_rota(pontos, n_geracoes=100, pop_size=100):
    n = len(pontos)

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("indices", random.sample, range(n), n)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def avaliar(ind):
        return (calcular_distancia(pontos, ind),)

    toolbox.register("evaluate", avaliar)
    toolbox.register("mate", tools.cxOrdered)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=pop_size)
    hof = tools.HallOfFame(1)

    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2,
                        ngen=n_geracoes, halloffame=hof, verbose=False)

    melhor = hof[0]
    return melhor, calcular_distancia(pontos, melhor)
