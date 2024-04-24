from gear import Gear
from player import Player
from loadout import Loadout

from itertools import product


def main(debug):
    if(not debug):
        print("Player Stats")
        basic_attack = float(input("Enter Player Basic Attack: "))
        crit_rate = float(input("Enter Player Crit Rate: "))
        crit_dmg = float(input("Enter Player Crit Damage: "))
        attack_speed = float(input("Enter Player Attack Speed: "))
        final_damage = float(input("Enter Player Final Damage: "))
        player = Player(basic_attack, crit_rate, crit_dmg, attack_speed, final_damage)
        gear_amount = int(input("Enter amount of gear pieces to compare: "))

        sword_list = []
        armor_list = []
        helmet_list = []
        gloves_list = []
        boots_list = []


        for gear in range(0, gear_amount):
            print(f"\n********************Item #{gear+1}********************")
            gear_type = int(input("Sword = 0, Armor = 1, Helmet = 2, Gloves = 3, Boots = 4\nEnter Gear Type: "))
            stats = []
            for i in range(0, 6):
                temp = []
                temp.append(int(input(f"BASIC_ATTACK = 0, CRIT_RATE = 1, CRIT_DMG = 2, ATTACK_SPEED = 3, FINAL_DAMAGE = 4\nEnter gear stat type: ")))
                temp.append(float(input(f"Enter gear stat {i+1}: ")))
                stats.append(temp)

            if(gear_type == 0):
                sword_list.append(Gear(gear_type, stats))
            elif(gear_type == 1):
                armor_list.append(Gear(gear_type, stats))
            elif(gear_type == 2):
                helmet_list.append(Gear(gear_type, stats))
            elif(gear_type == 3):
                gloves_list.append(Gear(gear_type, stats))
            elif(gear_type == 4):
                boots_list.append(Gear(gear_type, stats))

    if(debug):
        sword1 = Gear(0,[[0,1],[0,1],[0,1],[0,1],[0,1],[4,1]])
        sword2 = Gear(0,[[0,2],[0,2],[0,2],[0,2],[0,2],[0,2]])
        armor1 = Gear(1,[[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]])
        helmet1 = Gear(2,[[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]])
        gloves1 = Gear(3,[[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]])
        boots1 = Gear(4,[[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]])
        sword_list = [sword1,sword2]
        armor_list = [armor1]
        helmet_list = [helmet1]
        gloves_list = [gloves1]
        boots_list = [boots1]
        player = Player(10,10,10,10,10)


    product_list = list(product(sword_list, armor_list, helmet_list, gloves_list, boots_list))

    loadouts = []
    i = 0
    for loadout in product_list:
        loadouts.append(Loadout(player, loadout))
        print(f"\n***Loadout #{i+1}***")
        i += 1
        for item in loadout:
            item.print()

    i = 0
    for loadout in loadouts:
        print(f"\nFULL LOADOUT #{i+1}\n")
        loadout.print()
        i += 1


    #'a=baseAttack x attackSpeedPowerCalc x finalDamage x (1-critRate+critRate x ((1-superCritRate) x critDamage+superCritRate x superCritDamage));
    #(base_attack*MIN(attack_speed,400%)*L6*(1-MIN(L3,100%)+MIN(L3,100%)*((1-J7)*(J8*3)+1+J7*(J8*3)+1)))*J9

    for loadout in loadouts:
        part1 = loadout.basic_attack * min(loadout.attack_speed, 400) * loadout.final_damage
        part2 = 1 - loadout.crit_rate * ((1 - loadout.super_crit_rate) * loadout.crit_damage + loadout.super_crit_rate * loadout.super_crit_damage)
        damage = part1 * part2




    

if __name__ == "__main__":
    debug = False
    main(debug)