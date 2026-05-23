class character:
    name = None
    health = 100
    magicPoints = 100
    
    def __init__(self, name):
        self.name = name
        
    def print(self):
        print(f"{self.name}\t HP: {self.health}\t MP: {self.magicPoints}")
        print()
        
    def setStats(self, health, magicPoints):
        self.health = health
        self.magicPoints = magicPoints
        
class player(character):
    nickname = None
    lives = 3
    
    def __init__(self, nickname):
        self.name = "Player"
        self.nickname = nickname
        
    def print(self):
        print(f"{self.name}\t HP: {self.health}\t MP: {self.magicPoints}\t Nickname: {self.nickname} \tLives: {self.lives}")    
        print()
            
    def isAlive(self):
        if self.lives > 0:
            print(f"{self.nickname} lives on!")
            return True
        else:
            print(f"{self.nickname} has expired")
            return False
            
ian = player("Ian the Mighty")
ian.print()
print(ian.isAlive())

class enemy(character):
    type = None
    strength = None
        
    def __init__(self, name,  type, strength):
        self.name = name
        self.type = type
        self.strength = strength
        
    def print(self):
        print(f"{self.name}\t HP: {self.health}\t MP: {self.magicPoints}\t Type: {self.type} \tStrength: {self.strength}")
        print()    
        
class orc(enemy):
    speed = None
    
    def __init__(self, speed):
        self.name = "Orc"
        self.type = "Orc"
        self.strength = 200
        self.speed = speed
        
    def print(self):
        print(f"{self.name}\t HP: {self.health}\t MP: {self.magicPoints}\t Type: {self.type} \tStrength: {self.strength} \tSpeed: {self.speed}")
        print()
       
sharron = orc(250)
gary = orc(205)

sharron.print()
gary.print()

class vampire(enemy):
    day = True
    
    def __init__(self, day):
        self.name = "Vampire"
        self.type = "Vampire"
        self.strenth = 150
        self.day = day
        
    def print(self):
        print(f"{self.name}\t HP: {self.health}\t MP: {self.magicPoints}\t Type: {self.type} \tDay: {self.day} ")
        print()
        
eric = vampire(False)
eric.print()