from planet import Planet
from star import Star

SUN = Star(1.0)


def test_earth_mass():
    planet = Planet(SUN)
    planet.mass = 1.0
    assert planet.earth_mass() == 332775.64


def test_density():
    assert Planet(SUN).density() is None


def test_radius():
    assert Planet(SUN).radius() is None


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
