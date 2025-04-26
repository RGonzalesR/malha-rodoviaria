import networkx as nx

def count_triangles(G):
    """
    Conta número de triângulos na rede.
    """
    triangles = sum(nx.triangles(G).values())
    return triangles

def count_squares(G):
    """
    Conta número aproximado de quadrados na rede.
    (Forma simplificada - existem formas mais precisas)
    """
    count = 0
    for node in G:
        neighbors = set(G.neighbors(node))
        for n1 in neighbors:
            for n2 in neighbors:
                if n1 < n2 and G.has_edge(n1, n2):
                    mutual = set(G.neighbors(n1)) & set(G.neighbors(n2))
                    mutual.discard(node)
                    count += len(mutual)
    return count // 2