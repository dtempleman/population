import pandas as pd
from pathlib import Path
import json


DATA_DIR = Path('data')
RACE_DIR = DATA_DIR / 'races'


class Race():

    def __init__(self, name, adulthood, life_expenctantcy):
        self.name = name
        self.adulthood = adulthood
        self.life_expectantcy = life_expenctantcy
        self.compatibility = []

    def __str__(self):
        return f"{self.name}, {self.adulthood}, {self.life_expectantcy}, {[r.name for r in self.compatibility]}"

    def setup_compatibility(self, races):
        race_path = RACE_DIR / f"{self.name}.json"
        if race_path.is_file():
            json_blob = json.load(race_path.open())
            self.compatibility = [races[name] for name in json_blob.pop("compatibility", None)]
            self.compatibility.append(self)
                
    @classmethod
    def load_json(cls, json_path):
        json_blob = json.load(json_path)
        json_blob.pop("compatibility", None)
        return cls(**json_blob)
    



def load_all_races():
    races = {}
    for i, json_path in enumerate(RACE_DIR.glob("*.json")):
        race = Race.load_json(json_path.open())
        races[race.name] = race
    for r in races:
        races[r].setup_compatibility(races)

    return races
