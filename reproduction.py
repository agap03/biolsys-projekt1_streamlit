# reproduction.py

import copy
import numpy as np

def asexual_reproduction(survivors, N):
    """
    Wersja bezpłciowa (klonowanie):
    - Zakładamy, że potomków będzie tyle, aby utrzymać rozmiar populacji = N.
    - W najprostszej wersji: jeżeli mamy M ocalałych, 
      a M < N, to klonujemy ich losowo aż do uzyskania N osobników.
    """
    new_population = []
    if len(survivors) == 0:
        # Zabezpieczenie: jeśli wszyscy wymarli, inicjujemy od nowa (albo zatrzymujemy symulację).
        return []

    active_survivors=[]
    for ind in survivors:
        if ind.is_hibernated(): # jeśli w hibernacji
            ind.update_hibernation()
            new_population.append(ind)

            if ind.get_hibernation()==0: # jeśli właśnie się wybudził
                ind.update_just_awaken()

        else:
            active_survivors.append(ind)

    if len(active_survivors)==0:
        return new_population[:N]

    while len(new_population) < N:
        
        # klonowanie losowe
        parent = copy.deepcopy(np.random.choice(active_survivors))
        new_population.append(parent)


    return new_population[:N]  # przycinamy, gdyby było za dużo
