from pathlib import Path
import json
import numpy as np
from dataclasses import dataclass


DATA_DIR = Path('data')
RACE_DIR = DATA_DIR / 'races'


@dataclass
class Race():
    name: str
    adulthood: int
    life_expectantcy: int

    def __str__(self):
        return f"{self.name}, {self.adulthood}, {self.life_expectantcy}"


def random_normalized_age(race):
    mu = race.adulthood + int(race.life_expectantcy / 10)
    sigma = int(race.life_expectantcy / 15)
    return int(np.random.normal(mu, sigma))


def load_race_form_json(json_path):
    json_blob = json.load(json_path)
    json_blob.pop("compatibility", None)
    return Race(**json_blob)


def load_all_races():
    races = {}
    for _, json_path in enumerate(RACE_DIR.glob("*.json")):
        race = load_race_form_json(json_path.open())
        races[race.name] = race
    return races


# TODO: this should return all compatibilites rather than jsut for a given race
"""
def setup_compatibility(self, races):
    race_path = RACE_DIR / f"{self.name}.json"
    if race_path.is_file():
        json_blob = json.load(race_path.open())
        self.compatibility = [races[name] for name in json_blob.pop("compatibility", None)]
        self.compatibility.append(self)
"""
