from gear import Gear
from player import Player
from loadout import Loadout

from itertools import product
import pandas as pd


def main():
    mode = int(input("Enter 0 to upload spreadsheet or 1 to manualy enter: "))

    debuff_34 = [0, 75, 877.34, 225, 0]
    debuff_33 = [0, 70, 807.34, 210, 0]
    debuff_32 = [0, 65, 734.97, 195, 0]
    debuff_0 = [0, 0, 0, 0, 0]

    if(mode):
        product_list = input_gear_manually()
        player = input_player_manually(debuff_0)
    else:
        product_list = input_gear_spreadsheet()
        player = input_player_spreadsheet(debuff_0)


    #create loadout class from each combination and add to loadout array(dont like the naming for this loop can probable combine with next loop)
    loadouts = []
    i = 0
    print_all = False
    for loadout in product_list:
        full_loadout = Loadout(player, loadout)
        loadouts.append(full_loadout)
        if(print_all):
            print(f"\n*****Loadout #{i+1}*****")
            full_loadout.print(0)
        
        i += 1


    highest_power = 0
    highest_power_index = -1


    for i in range(0, len(loadouts)):
        if(loadouts[i].combat_power > highest_power):
            highest_power_index = i
            highest_power = loadouts[i].combat_power
        

    loadouts[highest_power_index].print(1)

    if(False):
        top_five(loadouts)

    if(False):
        while(True):
            choice = int(input(f"\nWhich loadout would you like to see gear for (1 to {len(loadouts)} or 0 to close): "))
            if(choice in range(1, len(loadouts) + 1)):
                loadouts[choice - 1].print(1)
            else:
                break


#Prints all gear that is not in top 5 for debuff
def top_five(loadouts) -> None:
    highest_power = 0
    highest_power2 = 0
    highest_power3 = 0
    highest_power4 = 0
    highest_power5 = 0
    highest_power_index = -1
    highest_power_index2 = -1
    highest_power_index3 = -1
    highest_power_index4 = -1
    highest_power_index5 = -1

    for i in range(0, len(loadouts)):
        if(loadouts[i].combat_power > highest_power):
            highest_power_index5 = highest_power_index4
            highest_power_index4 = highest_power_index3
            highest_power_index3 = highest_power_index2
            highest_power_index2 = highest_power_index
            highest_power_index = i
            
            highest_power5 = highest_power4
            highest_power4 = highest_power3
            highest_power3 = highest_power2
            highest_power2 = highest_power
            highest_power = loadouts[i].combat_power
            
        elif(loadouts[i].combat_power > highest_power2):
            highest_power_index5 = highest_power_index4
            highest_power_index4 = highest_power_index3
            highest_power_index3 = highest_power_index2
            highest_power_index2 = i

            highest_power5 = highest_power4
            highest_power4 = highest_power3
            highest_power3 = highest_power2
            highest_power2 = loadouts[i].combat_power

        elif(loadouts[i].combat_power > highest_power3):
            highest_power_index5 = highest_power_index4
            highest_power_index4 = highest_power_index3
            highest_power_index3 = i
            
            highest_power5 = highest_power4
            highest_power4 = highest_power3
            highest_power3 = loadouts[i].combat_power

        elif(loadouts[i].combat_power > highest_power4):      
            highest_power_index5 = highest_power_index4
            highest_power_index4 = i
            
            highest_power5 = highest_power4
            highest_power4 = loadouts[i].combat_power
        elif(loadouts[i].combat_power > highest_power5):
            highest_power_index5 = i
            highest_power5 =loadouts[i].combat_power

    for i in range(0, len(loadouts)):
        if(i == highest_power_index or
           i == highest_power_index2 or
           i == highest_power_index3 or
           i == highest_power_index4 or
           i == highest_power_index5):
            for item in loadouts[i].items:
                item.keep = True

    for i in range(0, len(loadouts)):
        for item in loadouts[i].items:
            if(item.keep == False):
                if(item.marked == False):
                    item.print(1)
                    item.marked = True

def input_gear_spreadsheet() -> list:
    df = pd.read_excel('gear.xlsx')
    row = df.iloc[3].to_numpy()

    sword_list = []
    armor_list = []
    helmet_list = []
    gloves_list = []
    boots_list = []

    for i in range(0, df.shape[0]):
        row = df.iloc[i].to_numpy()
        if(row[0] == "sword"):
            row[0] = 0
            sword_list.append(Gear(row[0], [[row[1], row[2]],[row[3], row[4]],[row[5], row[6]],[row[7], row[8]],[row[9], row[10]],[row[11], row[12]]]))
        elif(row[0] == "armor"):
            row[0] = 1
            armor_list.append(Gear(row[0], [[row[1], row[2]],[row[3], row[4]],[row[5], row[6]],[row[7], row[8]],[row[9], row[10]],[row[11], row[12]]]))
        elif(row[0] == "helmet"):
            row[0] = 2
            helmet_list.append(Gear(row[0], [[row[1], row[2]],[row[3], row[4]],[row[5], row[6]],[row[7], row[8]],[row[9], row[10]],[row[11], row[12]]]))
        elif(row[0] == "gloves"):
            row[0] = 3
            gloves_list.append(Gear(row[0], [[row[1], row[2]],[row[3], row[4]],[row[5], row[6]],[row[7], row[8]],[row[9], row[10]],[row[11], row[12]]]))
        elif(row[0] == "boots"):
            row[0] = 4
            boots_list.append(Gear(row[0], [[row[1], row[2]],[row[3], row[4]],[row[5], row[6]],[row[7], row[8]],[row[9], row[10]],[row[11], row[12]]]))
        else:
            print("ERROR: Invalid gear type")

    #Take product of gear arrays to get every possible combination
    return list(product(sword_list, armor_list, helmet_list, gloves_list, boots_list))

def input_gear_manually() -> list:
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

    #Take product of gear arrays to get every possible combination
    return list(product(sword_list, armor_list, helmet_list, gloves_list, boots_list))

def input_player_manually(debuff) -> Player:
    #input player stats
    print("Player Stats")
    basic_attack = float(input("Enter Player Basic Attack: ")) - debuff[0]
    crit_rate = float(input("Enter Player Crit Rate: ")) - debuff[1]
    crit_dmg = float(input("Enter Player Crit Damage: ")) - debuff[2]
    attack_speed = float(input("Enter Player Attack Speed: ")) - debuff[3]
    final_damage = float(input("Enter Player Final Damage: ")) - debuff[4]
    super_crit_rate = float(input("Enter Player Super Crit Rate: "))
    super_crit_dmg = float(input("Enter Player Super Crit Damage: "))
    return Player(basic_attack, crit_rate, crit_dmg, attack_speed, final_damage, super_crit_rate, super_crit_dmg)

#hardcoded for now
def input_player_spreadsheet(debuff) -> Player:
    rune = 734.97 + 120.0452
    return Player(324470 - debuff[0], 40 - debuff[1], 1350 + rune - debuff[2], 32.75 - debuff[3], 288 - debuff[4], 29.79, 348)

if __name__ == "__main__":
    main()