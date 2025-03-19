# visualization.py

import matplotlib.pyplot as plt
import numpy as np

def plot_population(population, alpha, generation, save_path=None, show_plot=False):
    """
    Rysuje populację w 2D wraz z optymalnym fenotypem alpha.
    Można zarówno wyświetlać (show_plot=True),
    jak i zapisywać obraz (save_path != None).
    """
    x=[]
    y=[]
    x_h=[]
    y_h=[]

    for ind in population.get_individuals():
        if ind.is_hibernated():
            x_h.append(ind.get_phenotype()[0])
            y_h.append(ind.get_phenotype()[1])
        else:
            x.append(ind.get_phenotype()[0])
            y.append(ind.get_phenotype()[1])
    
    plt.figure(figsize=(5, 5))
    plt.scatter(x, y, label=f"Populacja aktywna, {len(x)}", alpha=0.7)
    plt.scatter(x_h, y_h, label=f"Populacja w hibernacji, {len(x_h)}", alpha=0.7, color='orange')
    plt.scatter([alpha[0]], [alpha[1]], color='red', label="Optimum", marker='X')
    plt.title(f"Pokolenie: {generation}")
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.legend()
    plt.tight_layout()
    
    if save_path is not None:
        plt.savefig(save_path)  # Zapis do pliku
    if show_plot:
        plt.show()
    else:
        # Jeśli nie chcesz pokazywać, to zamykaj figurę, 
        # żeby nie zapełniać pamięci
        plt.close()
