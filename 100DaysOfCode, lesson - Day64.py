class animal:
    species = None
    name = None
    sound = None
    
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
        
    def talk(self):
        print(f"""{self.name} says {self.sound}""")
        
class bird(animal):
    
    color = None
    
    def __init__(self, color):
        self.name = "Bird"
        self.species = "Avian"
        self.sound = "Tweet"
        self.color = color
        
dog = animal("Dog", "Canine", "Woof")
dog.talk()

cow = animal("Cow", "Bo Taurus", "Moo")
cow.talk()

polly = bird("Green")
polly.talk()
print(polly.color)