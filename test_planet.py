from planet import Planet
from star import Star

SUN = Star(1.0)


def test_earth_mass():
    planet = Planet(SUN)
    planet.mass = 1.0
    assert planet.earth_mass() == 332775.64
    planet.mass = planet.earth_in_solar_masses
    assert planet.earth_mass() == 1.0


def test_regular_density():
    planet = Planet(SUN)
    planet.mass = planet.earth_in_solar_masses
    assert planet.density() == 5.5
    planet.mass *= 2.0
    assert round(planet.density(), 2) == 6.0


def test_gas_giant_density():
    planet = Planet(SUN)
    planet.mass = planet.earth_in_solar_masses
    planet.gas_giant = True
    assert planet.density() == 1.2
    planet.mass *= 2.0
    assert round(planet.density(), 2) == 1.31


def test_radius():
    planet = Planet(SUN)
    planet.mass = planet.earth_in_solar_masses
    assert round(planet.radius(), 2) == 6377.89


def test_orbital_period():
    assert Planet(SUN).orbital_period() is None


def test_day():
    assert Planet(SUN).day() is None


def test_resonant_period():
    assert Planet(SUN).resonant_period() is None


def test_axial_tilt():
    assert Planet(SUN).axial_tilt() is None


def test_escape_velocity():
    assert Planet(SUN).escape_velocity() is None


def test_surface_acceleration():
    assert Planet(SUN).surface_acceleration() is None


def test_rms_velocity():
    assert Planet(SUN).rms_velocity() is None


def test_molecular_weight():
    assert Planet(SUN).molecular_weight() is None


def test_surface_gravity():
    assert Planet(SUN).surface_gravity() is None


def test_under_greenhouse_effect():
    assert Planet(SUN).under_greenhouse_effect() is False


def test_volatile_gas_inventory():
    assert Planet(SUN).volatile_gas_inventory() is None


def test_surface_pressure():
    assert Planet(SUN).surface_pressure() is None


def test_boiling_point():
    assert Planet(SUN).boiling_point() is None


def test_hydrosphere():
    assert Planet(SUN).hydrosphere() is None


def test_albedo():
    assert Planet(SUN).albedo() is None


def test_surface_temperature():
    assert Planet(SUN).surface_temperature() is None


def test_calculate_surface_temperature():
    assert Planet(SUN).calculate_surface_temperature() is None
