class Character:
    def __init__(self, name, species, classification, location):
        self.species = species
        self.classification = classification
    
class Hero(Character):
    def __init__(self, name, species, classification, location, nobility, virtue):
        self.species = species
        self.name = name
        self.classification = classification
        self.location = location
        self.nobility = nobility
        self.virtue = virtue

    def description(self):
        print(f"{self.name} is a {self.classification} with a nobility level of {self.nobility}")

class Villain(Character):
    def __init__(self, name, species, classification, location, cunning, badness):
        self.name = name
        self.species = species
        self.classification = classification
        self.location = location
        self.cunning = cunning
        self.badness = badness

    def description(self):
        print(f"{self.name} is a {self.classification} with the darkest soul and a cunning of {self.cunning}")

luke = Hero("Luke", "human", "jedi", "Tatooine", 10, 8)
boba_fett = Villain("Boba Fett", "human", "bounty hunter", "wherever there is profit", 8, 9)

boba_fett.description()
luke.description()