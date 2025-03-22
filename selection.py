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




def threshold_selection(population, alpha, sigma, threshold, hibernation_thresh, h_p, mu_h):
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

            if f < threshold: # jeśli za słaby fitness
                if ind.is_just_awaken(): # jeśli dopiero się obudził, ale nie przeżył
                    ind.update_just_awaken()

            else: # jeśli przeżył (fitness wystraczający)
                survivors.append(ind) 

                if f < hibernation_thresh and np.random.rand() < mu_h: # jeśli może zahibernować
                    ind.hibernate(np.random.geometric(f)) # czas hibernacji z rokładu geometrycznego, zależy od fintess    
                    population.add_hib()

                    if ind.is_just_awaken(): # jeśli dopiero się obudził, a znowu hibernuje
                        population.add_repeated_hib()

                if ind.is_just_awaken(): # jeśli dopiero się obudził, a przeżył
                    ind.update_just_awaken()
                    population.add_survived_hib()

        else:
            survivors.append(ind)
    return survivors
