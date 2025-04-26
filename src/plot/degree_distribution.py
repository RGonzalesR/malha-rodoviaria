import matplotlib.pyplot as plt
import networkx as nx

def plot_degree_distribution(G, cumulative=True):
    degrees = [d for n, d in G.degree()]
    plt.figure()
    if cumulative:
        sorted_degrees = sorted(degrees)
        yvals = [1 - (i/len(sorted_degrees)) for i in range(len(sorted_degrees))]
        plt.loglog(sorted_degrees, yvals, marker='o', linestyle='none')
        plt.ylabel('P(>k)')
    else:
        plt.hist(degrees, bins=50, log=True)
        plt.ylabel('Frequency')
    plt.xlabel('Degree')
    plt.title('Degree Distribution')
    plt.grid(True)
    plt.show()