from population.being import Creature, calculate_age, check_death
from population.race import load_all_races, random_normalized_age
from world.time import increment_time_by_x_years


import random
import numpy as np
import tqdm


def generate_initial_random_population(population_size, current_year):
    races = load_all_races()
    print("Races:")
    for r in races:
        print(f"\t{r}: {races[r]}")
    print()

    population = []
    for i in range(population_size):
        race = random.choice(list(races.values()))
        # race = races['elf']
        age = random_normalized_age(race)
        birth_year = current_year - age

        creature = Creature(
            name=f"test {i}",
            race=race,
            birth_year=birth_year,
        )
        population.append(creature)
    return population


def increment_population_over_n_years(population, n, current_year):
    for i in tqdm.tqdm(range(n)):
        for pop in population:
            check_death(pop, increment_time_by_x_years(current_year, i))
    print(f"incremented {n} years.")


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
    # np.random.seed(seed)
    # random.seed(seed)

    current_year = random.randint(500, 5000)
    print(f"Current year: {current_year}")

    pop_size = 10
    population = generate_initial_random_population(pop_size, current_year)
    for creature in population:
        print(f'{creature}.\t\tAge {calculate_age(creature, current_year)}')

    years = 10000
    increment_population_over_n_years(population, years, current_year)
    current_year = current_year + years

    for pop in sorted(population, key=lambda x: calculate_age(x, current_year)):
        print(f'{pop.name} ({pop.race.name})\thas died at the age of {calculate_age(pop, current_year)} in the year {pop.death_year}')
