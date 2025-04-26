import networkx as nx

def load_mtx(filepath):
    G = nx.read_edgelist(filepath, comments='%', delimiter=' ', nodetype=int)
    return G