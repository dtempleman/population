from dataclasses import dataclass
from typing import List
from population.race import Race

import random


@dataclass
class Being():
    tags: List[str] = List


@dataclass
class Creature(Being):
    name: str = ""
    birth_year: int = 0
    death_year: int = -1
    race: Race = None
    parents: List[Being] = None
    children: List[Being] = None

    def __str__(self):
        return f"{self.name} - ({self.race}): born {self.birth_year}"

    def is_alive(self):
        if self.death_year > 0:
            return False
        return True 


def calculate_age(creature, current_year):
    if creature.is_alive():
        return current_year - creature.birth_year
    return creature.death_year - creature.birth_year


def calculate_death_by_old_age_chance(creature, current_year):
    death_chance = 0
    age = calculate_age(creature, current_year)

    if age - creature.race.adulthood > 0:
        r = creature.race.life_expectantcy - creature.race.adulthood
        # print(f'r = {r}')
        death_chance = (age - creature.race.adulthood) / r

    # print(f"{death_chance} at {age}")
    return death_chance


def check_death(creature, current_year):
    if creature.is_alive():
        x = random.uniform(0, 100)
        # print(f"x = {x}")
        if x <= calculate_death_by_old_age_chance(creature, current_year):
            creature.death_year = current_year
