# population.py

import numpy as np
from individual import Individual

class Population:
    """
    Klasa przechowuje listę osobników (Individual)
    oraz pomaga w obsłudze różnych operacji na populacji.
    """
    def __init__(self, size, n_dim):
        """
        Inicjalizuje populację losowymi fenotypami w n-wymiarach.
        :param size: liczba osobników (N)
        :param n_dim: wymiar fenotypu (n)
        """
        self.individuals = []
        for _ in range(size):
            # przykładowo inicjalizujemy fenotypy w okolicach [0, 0, ..., 0]
            phenotype = np.random.normal(loc=0.0, scale=1.0, size=n_dim)
            self.individuals.append(Individual(phenotype))
        
        self.survived_hib=0
        self.repeaded_hib=0
        self.total_hib=0

    def get_individuals(self):
        return self.individuals

    def set_individuals(self, new_individuals):
        self.individuals = new_individuals

    def add_survived_hib(self):
        self.survived_hib+=1

    def get_survived_hib(self):
        return self.survived_hib

    def add_hib(self):
        self.total_hib+=1

    def get_total_hib(self):
        return self.total_hib
    
    def add_repeated_hib(self):
        self.repeaded_hib+=1

    def get_repeated_hib(self):
        return self.repeaded_hib
