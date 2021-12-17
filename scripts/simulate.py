from numpy import array, dtype, ndarray
from numpy.core.fromnumeric import std
from numpy.random.mtrand import rand
from population.being import Creature, calculate_age
from population.race import load_all_races, random_normalized_age

import random
import numpy as np
import matplotlib.pyplot as plt


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
        race = random.choice(list(races.values()))
        age = random_normalized_age(race)
        birth_year = current_year - age

        creature = Creature(
            name="test",
            race=race,
            birth_year=birth_year,
        )
        population.append(creature)

    for creature in population:
        print(f'{creature}.\t\tAge {calculate_age(creature, current_year)}')


def role_age():
    dice_size = 6
    max_age = 80
    n_dice = int(max_age / dice_size + 1)

    roles = [random.randint(0, dice_size) for i in range(n_dice)]
    return sum(roles)


def truncate_normal_distribution(mean,  maxval, minval=0, stddev=1.0):
    return np.clip(np.random.normal(mean, stddev), minval, maxval)


if __name__ == "__main__":
    seed = 0
    #np.random.seed(seed)
    #random.seed(seed)

    generate_initial_population(10)
