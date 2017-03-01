import math

CM_PER_KM = 1.0e5


class Planet(object):
    earth_in_solar_masses = 1.0 / 332775.64

    def __init__(self, star):
        self.mass = 1.0  # Solar masses
        self.axis = 1.0
        self.gas_giant = False
        self.star = star

    def earth_mass(self):
        return self.mass / self.earth_in_solar_masses

    def density(self):
        factor = 1.2 if self.gas_giant else 5.5
        return factor * (
            self.earth_mass() ** (1.0 / 8.0)
        ) * (
            (self.star.ecosphere_radius() / self.axis) ** (1.0 / 4.0)
        )

    def radius(self):
        grams = self.mass * self.star.solar_mass_in_grams
        volume = grams / self.density()
        return (((3.0 / (math.pi * 4.0)) * volume) ** (1.0 / 3.0) / CM_PER_KM)

    def orbital_period(self):
        pass

    def day(self):
        pass

    def resonant_period(self):
        pass

    def axial_tilt(self):
        pass

    def escape_velocity(self):
        pass

    def surface_acceleration(self):
        pass

    def rms_velocity(self):
        pass

    def molecular_weight(self):
        pass

    def surface_gravity(self):
        pass

    def under_greenhouse_effect(self):
        return False

    def volatile_gas_inventory(self):
        pass

    def surface_pressure(self):
        pass

    def boiling_point(self):
        pass

    def hydrosphere(self):
        pass

    def albedo(self):
        pass

    def surface_temperature(self):
        pass

    def calculate_surface_temperature(self):
        pass
