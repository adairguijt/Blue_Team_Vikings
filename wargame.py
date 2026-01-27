# With a correction already implemented: dont forget to initialize an instance of Class "War"


from vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
great_war = War()

#Create 5 Vikings
for i in range(0,5):
    if i:
        great_war.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

#Create 5 Saxons
for i in range(0,5):
    if i:
        great_war.addSaxon(Saxon(100,random.randint(0,100)))
    
round = 0
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    great_war.vikingAttack()
    great_war.saxonAttack()
    print(f"round: {round} // Viking army: {len(great_war.vikingArmy)} warriors",f"and Saxon army: {len(great_war.saxonArmy)} warriors")
    print(great_war.showStatus())
    round += 1
    
    # Quick test to see if weather works
Soldier.WEATHER = "Foggy"
viking_test = Viking("Ragnar", 100, 50)
saxon_test = Saxon(100, 20)

print(f"Current Weather: {Soldier.WEATHER}")
# This might return 0 strength if the 20% fog miss triggers
print(f"Attack power in fog: {viking_test.attack()}")