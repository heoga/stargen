import math

CM_PER_KM = 1.0e5


class Planet(object):
    earth_in_solar_masses = 1.0 / 332775.64
    change_in_earth_angular_velocity = -1.3E-15  # rad/s
    earth_density = 5.52  # g/cc
    earth_radius = 6.378E8  # cm

    def __init__(self, star):
        self.mass = 1.0  # Solar masses
        self.axis = 1.0
        self.gas_giant = False
        self.star = star
        self.eccentricity = 1.0

    def orbit_zone(self):
        if self.axis < self.star.frost_line():
            return 1
        if (
                (self.axis >= self.star.frost_line()) and
                (self.axis < self.star.gas_line())
        ):
            return 2
        return 3

    def earth_mass(self):
        return self.mass / self.earth_in_solar_masses

    def density(self):
        if self.gas_giant:
            return 1.2 * (
                self.earth_mass() ** (1.0 / 8.0)
            ) * (
                (self.star.ecosphere_radius() / self.axis) ** (1.0 / 4.0)
            )
        mass = self.mass * self.star.solar_mass_in_grams
        equat_radius = self.radius() * CM_PER_KM
        volume = (4.0 * math.pi * (equat_radius ** 3.0)) / 3.0
        return(mass / volume)

    def kothari_radius(self):
        orbital_zone = self.orbit_zone()
        if orbital_zone == 1:
            atomic_weight = 15.0
            atomic_number = 8.0
        else:
            atomic_weight = 10.0
            atomic_number = 5.0
        a1_20 = 6.485E12
        a2_20 = 4.0032E-8
        beta_20 = 5.71E12
        temp = atomic_weight * atomic_number
        temp = (
            2.0 * beta_20 * (self.star.solar_mass_in_grams ** (1.0 / 3.0))
        ) / (a1_20 * (temp ** (1.0 / 3.0)))
        temp2 = a2_20 * (atomic_weight ** (4.0 / 3.0)) * (
            self.star.solar_mass_in_grams ** (2.0 / 3.0)
        )
        temp2 = temp2 * (self.mass ** (2.0 / 3.0))
        temp2 = temp2 / (a1_20 * (atomic_number ** 2))
        temp2 = 1.0 + temp2
        temp = temp / temp2
        temp = (temp * (self.mass ** (1.0 / 3.0))) / CM_PER_KM
        return temp

    def radius(self):
        if self.gas_giant:
            grams = self.mass * self.star.solar_mass_in_grams
            volume = grams / self.density()
            return ((
                (3.0 / (math.pi * 4.0)) * volume
            ) ** (1.0 / 3.0) / CM_PER_KM)
        return self.kothari_radius()

    def orbital_period(self):
        return (
            365.256 * math.sqrt(self.axis ** 3) /
            (self.mass + self.star.mass_ratio)
        )

    def spin_resonance_factor(self):
        return (1.0 - self.eccentricity) / (1.0 + self.eccentricity)

    def base_angular_velocity(self):
        if self.gas_giant:
            k2 = 0.24
        else:
            k2 = 0.33
        return math.sqrt(
            2.0 * 1.46E-19 * self.mass * self.star.solar_mass_in_grams /
            (k2 * (self.radius() * CM_PER_KM) ** 2.0)
        )

    def tidal_rotational_deceleration(self):
        return (
            self.change_in_earth_angular_velocity *
            (self.density() / self.earth_density) *
            (self.radius() * CM_PER_KM / self.earth_radius) *
            (
                (self.earth_in_solar_masses * self.star.solar_mass_in_grams) /
                (self.mass * self.star.solar_mass_in_grams)
            ) *
            (self.star.mass_ratio ** 2.0) *
            (1.0 / (self.axis ** 6.0))
        )

    def day(self):
        tidal_locked = False
        year_in_hours = self.orbital_period() * 24.0
        angular_velocity = self.base_angular_velocity() + (
            self.tidal_rotational_deceleration() * self.star.age()
        )
        if angular_velocity <= 0.0:
            tidal_locked = True
        else:
            day_in_hours = 2 * math.pi / (3600.0 * angular_velocity)
            if day_in_hours >= year_in_hours:
                tidal_locked = True
        if tidal_locked:
            if self.eccentricity > 0.1:
                return self.spin_resonance_factor() * year_in_hours
            else:
                return year_in_hours
        return day_in_hours

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
