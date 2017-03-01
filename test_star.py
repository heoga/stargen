from star import Star


def test_star_mass():
    specified = Star(0.9)
    assert specified.mass_ratio == 0.9
    masses = set()
    for i in range(0, 100):
        masses.add(Star().mass_ratio)
    assert len(masses) > 1
    assert min(masses) >= 0.6
    assert max(masses) <= 1.3


def test_luminosity_ratio():
    assert round(Star(0.5).luminosity_ratio(), 3) == 0.062
    assert round(Star(0.75).luminosity_ratio(), 3) == 0.316
    assert Star(1.0).luminosity_ratio() == 1.0
    assert round(Star(1.5).luminosity_ratio(), 3) == 5.062
    assert round(Star(2.0).luminosity_ratio(), 3) == 16.971


def test_stellar_dust_limit():
    assert round(Star(1.0).stellar_dust_limit()) == 200.0
    assert round(Star(1.5).stellar_dust_limit()) == 229.0


def test_main_sequence_life():
    assert round(Star(1.0).main_sequence_life()) == 1e10
    assert round(Star(0.5).main_sequence_life()) == 80000000000
    assert round(Star(1.5).main_sequence_life()) == 2962962963


def test_maximum_star_age():
    assert round(Star(1.0).main_sequence_life()) == 1e10
    assert round(Star(1.0).maximum_star_age()) == 6000000000
    assert round(Star(0.1).main_sequence_life()) == 867505354334
    assert round(Star(0.1).maximum_star_age()) == 6000000000
    assert round(Star(10).main_sequence_life()) == 21081851
    assert round(Star(10).maximum_star_age()) == 21081851


def test_star_age():
    ages = set()
    for i in range(0, 100):
        ages.add(Star().star_age())
    assert len(ages) > 1
    assert min(ages) >= 1.0E9
    assert max(ages) <= 6.0E9


def test_ecosphere_radius():
    assert Star(0.5).ecosphere_radius() == 0.25
    assert round(Star(2).ecosphere_radius(), 2) == 4.12


def test_greenhouse_radius():
    assert Star(0.5).greenhouse_radius() == 0.2325
