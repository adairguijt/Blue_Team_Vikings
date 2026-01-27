import random

class Soldier:
    WEATHER = "Clear" # Class variable shared by all

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        # Accuracy check for Foggy weather
        if Soldier.WEATHER == "Foggy":
            if random.random() < 0.2:
                return 0
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        return f"{self.name} has died in act of combat"

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        return "A Saxon has died in combat"


# WAAAAAAAAAGH

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        
        # Terrain effect: Muddy fields cause misses
        if Soldier.WEATHER == "Muddy" and random.random() < 0.15:
            return f"{viking.name} slipped in the mud!"

        result = saxon.receiveDamage(viking.strength)
        
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
            
        return result

    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        
        if Soldier.WEATHER == "Muddy" and random.random() < 0.15:
            return "A Saxon slipped in the mud!"
        
        result = viking.receiveDamage(saxon.strength)
        
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
            
        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."
    pass


