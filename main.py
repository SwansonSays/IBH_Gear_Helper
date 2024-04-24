from gear import Gear
from player import Player
from loadout import Loadout

from itertools import product


def main(debug):
    if(not debug):
        #input player stats
        print("Player Stats")
        basic_attack = float(input("Enter Player Basic Attack: "))
        crit_rate = float(input("Enter Player Crit Rate: "))
        crit_dmg = float(input("Enter Player Crit Damage: "))
        attack_speed = float(input("Enter Player Attack Speed: "))
        final_damage = float(input("Enter Player Final Damage: "))
        player = Player(basic_attack, crit_rate, crit_dmg, attack_speed, final_damage)
        gear_amount = int(input("Enter amount of gear pieces to compare: "))

        #init gear arrays
        sword_list = []
        armor_list = []
        helmet_list = []
        gloves_list = []
        boots_list = []

        #Take user input on gear and input into gear arrays
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

    #hard coded gear stats for testing
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

    #Take product of gear arrays to get every possible combination
    product_list = list(product(sword_list, armor_list, helmet_list, gloves_list, boots_list))

    #create loadout class from each combination and add to loadout array(dont like the naming for this loop can probable combine with next loop)
    loadouts = []
    i = 0
    for loadout in product_list:
        loadouts.append(Loadout(player, loadout))
        print(f"\n***Loadout #{i+1}***")
        i += 1
        for item in loadout:
            item.print() #print each individual items stats

    #print each loadouts full stats
    i = 0
    for loadout in loadouts:
        print(f"\nFULL LOADOUT #{i+1}\n")
        loadout.print()
        i += 1
    

if __name__ == "__main__":
    debug = False
    main(debug)