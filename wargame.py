from vikingsClasses import Soldier, Viking, Saxon, War
import random

War.GAME_SPEED = 1.0
Soldier.WEATHER = "Muddy"

soldier_names = ["Ricki", "Adair", "Roy", "Swapnali", "Eric-with-a-C", "Erik-with-a-K", "Kate", "Javier", "Raya", "Assya"]
great_war = War()

for i in range(5):
    name = random.choice(soldier_names)
    health = 100
    strength = random.randint(50, 80)
    great_war.addViking(Viking(name, health, strength))

for i in range(5):
    health = 100
    strength = random.randint(30, 60)
    great_war.addSaxon(Saxon(health, strength))

print("\n" + "="*50)
print(f"THE GREAT WAR BEGINS (Weather: {Soldier.WEATHER})")
print("="*50)

input("\n   (The armies are ready. Press Enter to charge!)")

round_count = 0

while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    round_count += 1
    print(f"\n--- ROUND {round_count} ---")
    print(f"Vikings: {len(great_war.vikingArmy)} | Saxons: {len(great_war.saxonArmy)}")
    
    great_war.vikingAttack()
    
    if great_war.showStatus() != "Vikings and Saxons are still in the thick of battle.":
        break
        
    input("   (Press Enter to continue...)")

    great_war.saxonAttack()
    
    if great_war.showStatus() != "Vikings and Saxons are still in the thick of battle.":
        break

    input("   (Press Enter to continue...)")

print("\n" + "="*50)
print(great_war.showStatus())
print("="*50 + "\n")

input("   (Press Enter to close the battlefield...)")