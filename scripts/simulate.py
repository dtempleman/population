from population.citizen import Citizen
from population.race import load_all_races

import random


def generate_initial_population(population_size):
    current_year = random.randint(500, 5000)
    print(f"Current year: {current_year}")

    races = load_all_races()
    print(f"Races:")
    for r in races:
        print(f"\t{races[r]}")
    print()

    population = []
    for _ in range(population_size):
        cit = Citizen(
            random.choice(list(races.values())),
            current_year=current_year,
        )
        population.append(cit)

    for cit in population:
        print(f'{cit}. Age {cit.calculate_age(current_year)}')


if __name__ == "__main__":
    generate_initial_population(10)
    
    import numpy as np

    mu, sigma = 26, 10 # mean and standard deviation

    s = np.random.normal(mu, sigma, 10000)

    import matplotlib.pyplot as plt
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
            linewidth=2, color='r')
    plt.show()