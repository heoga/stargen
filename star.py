import random
import math


class Star(object):
    greenhouse_factor = 0.93
    solar_mass_in_grams = 1.989e33

    def __init__(self, mass_ratio=None, age=None):
        if mass_ratio:
            self.mass_ratio = mass_ratio
        else:
            self.mass_ratio = random.uniform(0.6, 1.3)
        self.specified_age = age

    def luminosity_ratio(self):
        if self.mass_ratio < 0.43:
            ratio = 0.23 * self.mass_ratio ** 2.3
        elif self.mass_ratio < 2:
            ratio = self.mass_ratio ** 4.0
        elif self.mass_ratio < 20:
            ratio = 1.5 * self.mass_ratio ** 3.5
        else:
            ratio = 3200.0 * self.mass_ratio
        return ratio

    def stellar_dust_limit(self):
        return 200.0 * self.mass_ratio ** (1.0 / 3.0)

    def main_sequence_life(self):
        return 1.0E10 * (self.mass_ratio / self.luminosity_ratio())

    def maximum_star_age(self):
        return min(self.main_sequence_life(), 6.0E9)

    def age(self):
        if self.specified_age is None:
            self.specified_age = random.uniform(1.0E9, self.maximum_star_age())
        return self.specified_age

    def ecosphere_radius(self):
        return math.sqrt(self.luminosity_ratio())

    def frost_line(self):
        return 4 * self.ecosphere_radius()

    def gas_line(self):
        return 15 * self.ecosphere_radius()

    def greenhouse_radius(self):
        return self.ecosphere_radius() * self.greenhouse_factor
