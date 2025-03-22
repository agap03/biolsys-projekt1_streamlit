# individual.py

import numpy as np

class Individual:
    """
    Klasa opisująca pojedynczego osobnika.
    Przechowuje wektor fenotypu w n-wymiarowej przestrzeni.
    """
    def __init__(self, phenotype):
        self.phenotype = phenotype
        self.hibernation = 0
        self.just_awaken = False

    def get_phenotype(self):
        return self.phenotype

    def set_phenotype(self, new_phenotype):
        self.phenotype = new_phenotype

    def hibernate(self, time):
        self.hibernation=time

    def update_hibernation(self):
        if self.hibernation>0: 
            self.hibernation-=1

    def get_hibernation(self):
        return self.hibernation
    
    def is_hibernated(self):
        return self.hibernation>0
    
    def is_just_awaken(self):
        return self.just_awaken
    
    def update_just_awaken(self):
        self.just_awaken=not self.just_awaken