import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from collections import Counter

def plot_degree_distribution(G, cumulative=True):
    degrees = [d for n, d in G.degree()]
    
    degree_counts = Counter(degrees)
    deg, cnt = zip(*sorted(degree_counts.items()))
    deg = np.array(deg)
    cnt = np.array(cnt)
    
    if cumulative:
        cumulative_cnt = np.cumsum(cnt[::-1])[::-1]  # Acumulando de trás para frente
        cumulative_prob = cumulative_cnt / cumulative_cnt[0]
        
        plt.plot(deg, cumulative_prob)
        plt.ylabel('P(>k)')
    else:
        plt.plot(deg, cnt)
        plt.ylabel('Frequência')

    plt.xlabel('Degree')
    plt.title('Degree Distribution')
    plt.grid(True)