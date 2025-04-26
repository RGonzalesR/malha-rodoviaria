import numpy as np
import networkx as nx

def search_information(G, source, target):
    """
    Calcula a search information S(s -> t)
    """
    if source == target:
        return 0.0

    paths = list(nx.all_shortest_paths(G, source=source, target=target))

    if not paths:
        return 0.0  # Assume 0 se não houver caminho

    total_prob = 0
    for path in paths:
        prob = 1 / G.degree(path[0])
        for node in path[1:-1]:
            prob *= 1 / (G.degree(node) - 1)
        total_prob += prob

    if total_prob <= 0:
        return 0.0

    S = -np.log2(total_prob)
    return S

def average_search_information(G):
    """
    Calcula a search information média para todos os pares (s, t)
    """
    nodes = list(G.nodes())
    n = len(nodes)
    S_total = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            try:
                S_total += search_information(G, nodes[i], nodes[j])
            except (nx.NetworkXNoPath, ZeroDivisionError):
                S_total += 0

    return S_total / (n * n)

def access_information(G):
    """
    Calcula o Access Information A(s)
    """
    nodes = list(G.nodes())
    n = len(nodes)
    access_info = {}

    for s in nodes:
        S_total = 0
        for t in nodes:
            try:
                S_total += search_information(G, s, t)
            except (nx.NetworkXNoPath, ZeroDivisionError):
                S_total += 0
        access_info[s] = S_total / n

    return access_info