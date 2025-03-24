import os
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from environment import Environment
from population import Population
from mutation import mutate_population
from selection import threshold_selection
from reproduction import asexual_reproduction
from visualization import plot_population
from run_simulation import create_gif_from_frames, run_simulation





def main():

    st.title("Model ewolucyjny w oparciu o Geometryczny Model Fishera (GMF)")

    st.markdown(
        """
        Model zakłada możliwość hibernacji osobnika.  
        Optimum zmienia się sinusoidalnie.
        """
    )

    st.sidebar.header("Parametry symulacji")

    # Inputs for the simulation
    N = st.sidebar.number_input("Rozmiar populacji (N)", min_value=1, max_value=500, step=1, value=100)
    mu = st.sidebar.number_input("Prawdopodobieństwo mutacji dla osobnika", min_value=0.0, max_value=1.0, value=0.1, step=0.01)
    mu_c = st.sidebar.number_input("Prawdopodobieństwo mutacji konkretnej cechy, jeśli osobnik mutuje", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    xi = st.sidebar.number_input("Odchylenie standardowe w rozkładzie normalnym mutacji", min_value=0.0, max_value=1.0, value=0.1, step=0.01)
    sigma = st.sidebar.number_input("Parametr w funkcji fitness (kontroluje siłę selekcji)", min_value=0.0, max_value=1.0, step=0.1, value=0.2)
    threshold = st.sidebar.number_input("Przykładowy próg do selekcji progowej (do ewentualnego użycia)", min_value=0.0, max_value=1.0, value=0.1, step=0.1)
    hibernation_thresh = st.sidebar.number_input("Próg hibernacji", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
    h_p = st.sidebar.number_input("Prawdopodobieństwo obudzenia się z hibernacji przy jednym pokoleniu", min_value=0.0, max_value=1.0, value=0.15, step=0.01)
    mu_h = st.sidebar.number_input("Prawdopodobieństwo hibernacji, gdy w dobrym progu", min_value=0.0, max_value=1.0, value=0.3, step=0.01)
    A = st.sidebar.number_input("Amplituda sinusoidalnej zmiany optymalnego fenotypu", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    B = st.sidebar.number_input("Okres sinusoidalnej zmiany optymalnego fenotypu", min_value=0.0, max_value=1.0, value=0.1, step=0.1)
    max_generations = st.sidebar.number_input("Liczba pokoleń do zasymulowania", min_value=1, max_value=1000, value=100, step=1)


    if st.sidebar.button("Run Simulation"):
        # Create a progress bar
        progress_bar = st.progress(0)
        with st.spinner("Running simulation... (please wait)"):
            surv_hib, rep_hib, hib= run_simulation(
                N,
                mu,
                mu_c,
                xi,
                sigma,
                threshold,
                hibernation_thresh,
                h_p,
                mu_h,
                A,
                B,
                max_generations,
                progress_bar
            )
    
        st.success(f"""Symulacja zakończona!   
                   Przeżyte hibernacje: {surv_hib}; Powtórzone hibernacje: {rep_hib}; Wszystkie hibernacje: {hib}""")

        if os.path.exists("hibernacje.png"):
            st.image("hibernacje.png")
        else:
            st.markdown("Brak pliku z liczbą hibernacji")

        if os.path.exists("simulation.gif"):
            st.image("simulation.gif")
        else:
            st.markdown("Brak pliku gif")

    return



if __name__ == "__main__":
    main()