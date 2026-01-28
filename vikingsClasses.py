import random
import time
import pygame

class Soldier:
    WEATHER = "Clear"

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        if Soldier.WEATHER == "Foggy":
            if random.random() < 0.2:
                return 0
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

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


class War:
    GAME_SPEED = 0.05 

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
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

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
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

        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."