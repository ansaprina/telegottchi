def normalize(i):
    if i > 100:
        i = 100
    return i


class Event:

    def __init__(self, event_type, name, happiness, health, satiety, energy):
        self.type = event_type
        self.name = name
        self.happiness = happiness
        self.health = health
        self.satiety = satiety
        self.energy = energy
