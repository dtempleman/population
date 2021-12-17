from dataclasses import dataclass
from typing import List
from population.race import Race


@dataclass
class Being():
    tags: List[str] = List


@dataclass
class Creature(Being):
    name: str = ""
    birth_year: int = 0
    race: Race = None
    parents: List[Being] = None
    children: List[Being] = None

    def __str__(self):
        return f"{self.name} - ({self.race}): born {self.birth_year}"


def calculate_age(creature, current_year):
    return current_year - creature.birth_year
