# main.py

import os
import numpy as np
import config
import matplotlib.pyplot as plt
from environment import Environment
from population import Population
from mutation import mutate_population
from selection import threshold_selection
from reproduction import asexual_reproduction
from visualization import plot_population

def main():
    env = Environment(alpha_init=config.alpha0, A=config.A, B=config.B)
    pop = Population(size=config.N, n_dim=config.n)

    # Katalog, w którym zapisujemy obrazki (możesz nazwać np. "frames/")
    frames_dir = "frames"
    os.makedirs(frames_dir, exist_ok=True)  # tworzy folder, jeśli nie istnieje

    opts=[]
    hibernated=[]

    for generation in range(config.max_generations):

        # 1. Mutacja
        mutate_population(pop, mu=config.mu, mu_c=config.mu_c, xi=config.xi)


        # 2. Selekcja
        survivors = threshold_selection(pop, env.get_optimal_phenotype(), config.sigma, config.threshold,  config.hibernation_thresh, config.h_p, config.mu_h)

        # 3. Reprodukcja
        new_pop=asexual_reproduction(survivors, config.N)

        pop.set_individuals(new_pop)

        if len(new_pop) <= 0:
            print(f"Wszyscy wymarli w pokoleniu {generation}. Kończę symulację.")
            break

        # 4. Zmiana środowiska
        env.update()


        # Zapis aktualnego stanu populacji do pliku PNG
        frame_filename = os.path.join(frames_dir, f"frame_{generation:03d}.png")
        plot_population(pop, env.get_optimal_phenotype(), generation, save_path=frame_filename, show_plot=False)
        
        no_hib=0
        for ind in pop.get_individuals():
            if ind.is_hibernated():
                no_hib+=1

        hibernated.append(no_hib)
        opts.append(env.get_optimal_phenotype()[0])
                

    print("Symulacja zakończona.")

    print("Przeżyte hibernacje: ", pop.get_survived_hib(), "; Powtórzone hibernacje: ", pop.get_repeated_hib(), "; Wszystkie hibernacje: ", pop.get_total_hib(), "\n")

    print("Tworzenie GIF-a...")

    # Tutaj wywołujemy funkcję, która połączy zapisane klatki w animację
    create_gif_from_frames(frames_dir, "simulation.gif")
    print("GIF zapisany jako simulation.gif")

    print("Tworzenie wykresu z liczbą hibernacji...")

    plt.figure(figsize=(5, 5))
    plt.scatter(opts, hibernated, alpha=0.7)
    plt.title(f"Liczba hibernacji w zależności od optimum")
    plt.xlim(-config.A-0.5, config.A+0.5)
    xlabels=np.linspace(-config.A, config.A, 7)
    plt.xticks(xlabels, [f"({x:.1f}, {x:.1f})" for x in xlabels], rotation ='vertical')
    plt.xlabel("Optimum")
    plt.ylabel("Liczba osobników w hibernacji")
    plt.tight_layout()
    plt.savefig("hibernacje.png")

    print("Liczba hibernacji zapisana jako hibernacje.png")

def create_gif_from_frames(frames_dir, gif_filename, duration=0.2):
    """
    Łączy wszystkie obrazki z katalogu `frames_dir` w jeden plik GIF.
    Wymaga biblioteki imageio (pip install imageio).
    :param frames_dir: folder z plikami .png
    :param gif_filename: nazwa pliku wyjściowego GIF
    :param duration: czas wyświetlania jednej klatki w sekundach
    """
    import imageio
    import os

    # Sortujemy pliki po nazwach, żeby zachować kolejność generacji
    filenames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])
    
    with imageio.get_writer(gif_filename, mode='I', duration=duration) as writer:
        for file_name in filenames:
            path = os.path.join(frames_dir, file_name)
            image = imageio.imread(path)
            writer.append_data(image)


if __name__ == "__main__":
    main()
