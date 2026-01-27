import random

# Weapon

class Weapon:
    # Weapon constructor
    def __init__(self, name, min_damage, max_damage, crit_chance=0.0):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.crit_chance = crit_chance

    # Waepon damage
    def weapon_damage(self):
        damage = random.randint(self.min_damage, self.max_damage)

        # random.random() to generate float between 0.0 - 1.0
        if random.random() < self.crit_chance:
            damage *= 2
        return damage

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

        # new addition, default is no weapon, (should not break the test)
        self.weapon = None
    
    # if Soldier has a weapon -> use the Weapon damage+crit, else use the strength
    def attack(self):
        if self.weapon is not None:
            return self.weapon.weapon_damage()
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name  = name
        super().__init__(health,strength)

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# WAAAAAAAAAGH

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        # now add Weapon damage (if Soldier has weapon)
        damage = viking.attack()
        result = saxon.receiveDamage(damage)

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)        

        # here also add weapon damage
        damage = saxon.attack()
        result = viking.receiveDamage(damage)

        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


