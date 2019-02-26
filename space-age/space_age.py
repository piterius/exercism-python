PLANETS = {"mercury": 0.2408467, "venus": 0.61519726, "earth": 1, "mars": 1.8808158, "jupiter": 11.862615,
           "saturn": 29.447498, "uranus": 84.016846, "neptune": 164.79132}


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.years = seconds / (60 * 60 * 24 * 365.25)
        for planet, count in PLANETS.items():
            setattr(self, "on_" + planet, lambda x=count: round(self.years / x, 2))
