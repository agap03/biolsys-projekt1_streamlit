# environment.py

import numpy as np

class Environment:
    """
    Klasa środowiska przechowuje optymalny fenotyp alpha
    oraz reguły jego zmiany w czasie.
    """
    def __init__(self, alpha_init, A, B):
        """
        :param alpha_init: początkowy wektor alpha
        :param A: amplituda
        :param B: okres
        """
        self.alpha = alpha_init
        self.A = A
        self.B = B
        self.t=0 # krok czasowy

    def update(self):
        """
        Zmiana środowiska w każdym pokoleniu:
        alpha(t) = A * sin(B * t)
        """
        n=len(self.alpha)
        self.alpha = self.A * np.sin( self.B * self.t) * np.ones(n)
        self.t+=1

    def get_optimal_phenotype(self):
        return self.alpha
