import matplotlib.pyplot as plt
import networkx as nx

def graph_plot(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_size=10, edge_color='gray', with_labels=False)
    plt.show()