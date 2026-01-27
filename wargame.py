# With a correction already implemented: dont forget to initialize an instance of Class "War"


from vikingsClasses import Soldier, Viking, Saxon, War, Weapon
import random

# The Weapons
axe = Weapon("Axe", 15, 28, crit_chance=0.18)
sword = Weapon("Sword", 13, 22, crit_chance=0.10)
club = Weapon("Club", 11, 18, crit_chance=0.06)
spear = Weapon("Spear", 14, 20, crit_chance=0.10)

soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
great_war = War()


# this is 5 v 5 battle
# create 5 Vikings
for i in range(0,5):
    v = Viking(random.choice(soldier_names), 100, random.randint(3, 5))
    if random.random() < 0.7:
        v.weapon = random.choice([axe, sword, club, spear])
    else:
        v.weapon = None     # no weapon
    
    if v.weapon is not None:
        weapon_info = f"{v.weapon.name} ({v.weapon.min_damage}-{v.weapon.max_damage}, crit={v.weapon.crit_chance})"
    else:
        weapon_info = "bare hands"

    great_war.addViking(v)
    print(f"Viking {v.name} joins with {weapon_info} (health={v.health}, strength={v.strength})")


# create 5 Saxons
for _ in range(0,5):
    s = Saxon(100, random.randint(3, 5))
    if random.random() < 0.7:
        s.weapon = random.choice([axe, sword, club, spear])
    else:
        s.weapon = None    # no weapon
    
    if s.weapon is not None:
        weapon_info = f"{s.weapon.name} ({s.weapon.min_damage}-{s.weapon.max_damage}, crit={s.weapon.crit_chance})"
    else:
        weapon_info = "bare hands"
    great_war.addSaxon(s)
    print(f"a Saxon joins with {weapon_info} (health={s.health}, strength={s.strength})")

round = 0
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":

    # add Battle Log for Vikings
    if len(great_war.vikingArmy) > 0 and len(great_war.saxonArmy) > 0:
        v_msg = great_war.vikingAttack()
        print("Viking attack result:", v_msg)
        print("Saxons left:", len(great_war.saxonArmy))
    
    # add Battle Log for Saxons
    if len(great_war.vikingArmy) > 0 and len(great_war.saxonArmy) > 0:
        s_msg = great_war.saxonAttack()
        print("Saxon attack result:", s_msg)
        print("Vikings left:", len(great_war.vikingArmy))


    print(f"round: {round} // Viking army: {len(great_war.vikingArmy)} warriors",f"and Saxon army: {len(great_war.saxonArmy)} warriors")
    print(great_war.showStatus())
    round += 1