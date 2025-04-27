import networkx as nx
import osmnx as ox

def load_mtx(filepath):
    G = nx.read_edgelist(filepath, comments='%', delimiter=' ', nodetype=int)
    return G

def load_graph_from_place(place):
    """
    Através da lib OSMNX, carrega o grafo de uma malha viária
    Retorna como grafo simples com arestas não direcionais
    """
    G = ox.graph_from_place(place, network_type='drive')
    G = G.to_undirected()
    G = nx.Graph(G)
    
    return G