class Clock:

    def __init__(self, hours, minutes):
        self.minutes = (hours * 60 + minutes) % 1440

    def __repr__(self):
        return str(self.minutes // 60).zfill(2) + ":" + str(self.minutes % 60).zfill(2)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        self.minutes = (self.minutes + minutes) % 1440
        return self

    def __sub__(self, minutes):
        self.minutes = (self.minutes - minutes) % 1440
        return self