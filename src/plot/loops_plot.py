import matplotlib.pyplot as plt

def plot_loops(k_values, triangles_ratio, squares_ratio):
    plt.figure()
    plt.plot(k_values, triangles_ratio, 'o-', label='Triangles')
    plt.plot(k_values, squares_ratio, 's-', label='Squares')
    plt.xscale('log')
    plt.xlabel('Degree k')
    plt.ylabel('Normalized number of loops')
    plt.legend()
    plt.grid(True)
    plt.title('Loops vs Degree')
    plt.show()