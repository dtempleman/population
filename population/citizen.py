import random


class Citizen:

    def __init__(self, race, birth_year=None, current_year=None):
        self.race = race

        # generate a birth year
        if birth_year is not None:
            self.birth_year = birth_year
        elif current_year is not None:
            self.birth_year = self._calculate_birth_year(current_year)
        else:
            self.birth_year = 0

        self.parents = []
        self.children = []
    
    def __str__(self):
        return f"{self.race}: born {self.birth_year}"

    def death_chance(self, current_year):
        # calculate the chance of death based on age and liniage
        pass

    def calculate_age(self, current_year):
        return current_year - self.birth_year

    def race(self):
        return self.race

    def _calculate_birth_year(self, current_year):
        # get age on a normal curve
        return current_year - self._calculate_age_on_curve()
    
    def _calculate_age_on_curve(self):
        return random.randint(0, self.race.life_expectantcy)
