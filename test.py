from loadout import Loadout
from player import Player
from gear import Gear


#hard coded gear and player stats for testing
sword = Gear(0, [[0,1040184],[1,8.71],[2,0],[3,0],[4,262.35]])
armor = Gear(1, [[0,94867],[1,8.80],[2,378.13],[3,0],[4,965.36]])
helmet = Gear(2, [[0,90834],[1,85.03],[2,180.23],[3,0],[4,255.09]])
gloves = Gear(3, [[0,180047],[1,0],[2,2162.68],[3,0],[4,85.58]])
boots = Gear(4, [[0,259847],[1,0],[2,0],[3,494.54],[4,83.60]])
gear = [sword, armor, helmet, gloves, boots]
player = Player(468682,40,1920.00,40.00,338.10,34.81,397.10)


loadout = Loadout(player, gear)

loadout.print()

#Damage formula from spreadsheet
crit_ratio = min(loadout.crit_rate, 100) * (100 - loadout.super_crit_rate) / 100
super_crit_ratio = min(loadout.crit_rate, 100) * loadout.super_crit_rate / 100
hit_ratio = 100 - crit_ratio - super_crit_ratio

base_dmg = loadout.basic_attack * (loadout.final_damage / 100) * 1.25
damage_crit = loadout.crit_dmg / 100 * base_dmg
damage_super_crit = loadout.super_crit_dmg / 100 * base_dmg

total_dmg = (damage_crit * crit_ratio / 100) + (damage_super_crit * super_crit_ratio / 100) + (base_dmg * hit_ratio / 100)

combat_power = min(loadout.attack_speed, 400) / 100 * total_dmg

#Print damage values and compare with expected damage
print("\n")
print(f"crit ratio: {round(crit_ratio, 2)} | {crit_ratio - 65.19}")
print(f"super crit ratio: {round(super_crit_ratio, 2)} | {super_crit_ratio - 34.81}")
print(f"hit ratio: {round(hit_ratio, 2)} | {hit_ratio - 0.00}")
print(f"base dmg: {round(base_dmg, 2)} | 55764928.09 | {base_dmg - 55764928.09}")
print(f"damage crit: {round(damage_crit, 2)} | 2643837546.53 | {damage_crit - 2643837546.53}")
print(f"damage super crit: {round(damage_super_crit, 2)} | 13142516443.79 | {damage_super_crit - 13142516443.79}")
print(f"total: {round(total_dmg, 2)} | 6298427670.67 | {total_dmg - 6298427670.67}")
print(f"power: {round(combat_power, 2)} | 25193710682.67 | {combat_power - 25193710682.67}")
print(f"power: {round(combat_power / 1000, 2)}a") 
print(f"power: {round(combat_power / 1000000, 2)}b") 
print(f"power: {round(combat_power / 1000000000, 2)}c") 