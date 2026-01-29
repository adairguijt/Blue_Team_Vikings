import random
<<<<<<< HEAD
import time
import pygame
=======

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

>>>>>>> 733af45ac581996e53e5fe093a5d5feb3ba205aa

class Soldier:
    WEATHER = "Clear"

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

        # new addition, default is no weapon, (should not break the test)
        self.weapon = None
    
    # if Soldier has a weapon -> use the Weapon damage+crit, else use the strength
    def attack(self):
<<<<<<< HEAD
        if Soldier.WEATHER == "Foggy":
            if random.random() < 0.2:
                return 0
=======
        if self.weapon is not None:
            return self.weapon.weapon_damage()
>>>>>>> 733af45ac581996e53e5fe093a5d5feb3ba205aa
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

    

class Viking(Soldier):
    def __init__(self, name, health, strength):
<<<<<<< HEAD
        super().__init__(health, strength)
        self.name = name
=======
        self.name  = name
        super().__init__(health,strength)
>>>>>>> 733af45ac581996e53e5fe093a5d5feb3ba205aa

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
<<<<<<< HEAD
        return f"{self.name} has died in act of combat"
=======
        else:
            return f"{self.name} has died in act of combat"
>>>>>>> 733af45ac581996e53e5fe093a5d5feb3ba205aa


class Saxon(Soldier):
    def __init__(self, health, strength):
<<<<<<< HEAD
        super().__init__(health, strength)
=======
        super().__init__(health,strength)
>>>>>>> 733af45ac581996e53e5fe093a5d5feb3ba205aa

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
<<<<<<< HEAD
        return "A Saxon has died in combat"
=======
        else:
            return f"A Saxon has died in combat"
>>>>>>> 733af45ac581996e53e5fe093a5d5feb3ba205aa


class War:
    GAME_SPEED = 0.05 

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
<<<<<<< HEAD
        
        pygame.mixer.init()
        try:
            self.snd_start = pygame.mixer.Sound("start.wav")
            self.snd_swing = pygame.mixer.Sound("swing.wav")
            self.snd_slip = pygame.mixer.Sound("slip.wav")
            self.snd_hit = pygame.mixer.Sound("hit.wav")
            self.snd_kill = pygame.mixer.Sound("kill.wav")
            self.snd_win = pygame.mixer.Sound("win.wav")
        except:
            pass
        
        try:
            self.snd_start.play()
        except:
            pass
=======
>>>>>>> 733af45ac581996e53e5fe093a5d5feb3ba205aa

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
<<<<<<< HEAD
        if not self.saxonArmy:
            return "No Saxons left to fight!"
        if not self.vikingArmy:
            return "No Vikings left to attack!"
        
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        
        print(f"\n   🪓 {viking.name} raises a heavy axe...")
        try: self.snd_swing.play()
        except: pass
        
        time.sleep(War.GAME_SPEED)
        
        if Soldier.WEATHER == "Muddy" and random.random() < 0.2:
            try: self.snd_slip.play()
            except: pass
            print(f"      ❌ {viking.name} slipped in the mud and missed!")
            return f"{viking.name} slipped in the mud"

        result = saxon.receiveDamage(viking.strength)
        
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
            try: self.snd_kill.play()
            except: pass
            print(f"      💀 CRITICAL HIT! {result}")
        else:
            try: self.snd_hit.play()
            except: pass
            print(f"      💥 {result}")
            
        return result

    def saxonAttack(self):
        if not self.vikingArmy:
            return "No Vikings left to fight!"
        if not self.saxonArmy:
            return "No Saxons left to attack!"

        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        
        print(f"\n   🛡️ A Saxon thrusts a rusty spear at {viking.name}...")
        try: self.snd_swing.play()
        except: pass
        
        time.sleep(War.GAME_SPEED)

        if Soldier.WEATHER == "Muddy" and random.random() < 0.2:
            try: self.snd_slip.play()
            except: pass
            print("      ❌ The Saxon slipped on wet grass and missed!")
            return "A Saxon slipped in the mud"
        
        result = viking.receiveDamage(saxon.strength)
        
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
            try: self.snd_kill.play()
            except: pass
            print(f"      🪦 TRAGEDY! {result}")
        else:
            try: self.snd_hit.play()
            except: pass
            print(f"      🩸 {result}")
            
        return result

    def showStatus(self):
        print("\n" + "⚔️ " * 20)
        
        if not self.saxonArmy:
            try: self.snd_win.play()
            except: pass
            print("🏆 VICTORY! The Vikings have won the war of the century!")
        elif not self.vikingArmy:
            print("🏰 DEFEAT! The Saxons have survived another day...")
        else:
            print(f"   The battle rages on... (Vikings: {len(self.vikingArmy)} | Saxons: {len(self.saxonArmy)})")
            
        print("⚔️ " * 20 + "\n")
=======
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

>>>>>>> 733af45ac581996e53e5fe093a5d5feb3ba205aa

        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."