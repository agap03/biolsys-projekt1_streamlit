# selection.py

import numpy as np

def fitness_function(phenotype, alpha, sigma):
    """
    Funkcja fitness: phi_alpha(p) = exp( -||p - alpha||^2 / (2*sigma^2) )
    :param phenotype: fenotyp osobnika (np.array)
    :param alpha: optymalny fenotyp (np.array)
    :param sigma: odchylenie (float) kontrolujące siłę selekcji
    """
    diff = phenotype - alpha
    dist_sq = np.sum(diff**2)
    return np.exp(-dist_sq / (2 * sigma**2))



def threshold_selection(population, alpha, sigma, threshold, hibernation_thresh, h_time, mu_h):
    """
    Model progowy:
      - Eliminujemy osobniki, których fitness < threshold.
      - Pozostałe przechodzą do kolejnej fazy (o ile nie przekroczymy N).
      - Jeśli liczba ocalałych > N, wtedy dodatkowa redukcja.

      osobniki, których (treshhold < fitness < hibernation_thresh) hibernują z prawdopodobieństwem mu_h
    """
    individuals = population.get_individuals()
    survivors = []
    for ind in individuals:
        if not ind.is_hibernated():
            f = fitness_function(ind.get_phenotype(), alpha, sigma)
            if f >= hibernation_thresh:
                survivors.append(ind)
            elif f >= threshold:
                if np.random.rand() < mu_h:
                    ind.hibernate(h_time)
                survivors.append(ind)
        else:
            survivors.append(ind)
    return survivors
