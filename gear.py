from enum import Enum

class GearType(Enum):
    SWORD = 0
    ARMOR = 1
    HELMET = 2
    GLOVES = 3
    BOOTS = 4

class StatType(Enum):
    BASIC_ATTACK = 0
    CRIT_RATE = 1
    CRIT_DMG = 2
    ATTACK_SPEED = 3
    FINAL_DAMAGE = 4

class Gear():
    def __init__(self, gear_type: int, stats: list) -> None:
        self.gear_type = self.validate_gear(gear_type)
        self.basic_attack = 0 
        self.crit_rate = 0
        self.crit_dmg = 0
        self.attack_speed = 0
        self.final_damage = 0
        self.process_stats(stats)


    '''Combines each affix into total amount of each stat'''
    def process_stats(self, stats: list) -> None:
        for stat in stats:
            if(stat[0] == 0):
                self.basic_attack += stat[1]
            elif(stat[0] == 1):
                self.crit_rate += stat[1]
            elif(stat[0] == 2):
                self.crit_dmg += stat[1]
            elif(stat[0] == 3):
                self.attack_speed += stat[1]
            elif(stat[0] == 4):
                self.final_damage += stat[1]
            else:
                print("ERROR!!!")

    def validate_gear(self, gear_type):
        if(not gear_type in range(0,5)):
            print("ERROR")
            return -1
        else:
            return gear_type

    def print(self) -> None:
        print("\n")
        if(self.gear_type == 0):
            print("Sword")
        elif(self.gear_type == 1):
            print("Armor")
        elif(self.gear_type == 2):
            print("Helmot")
        elif(self.gear_type == 3):
            print("Gloves")
        elif(self.gear_type == 4):
            print("Boots")
        else:
            print("ERROR!!!")

        print(f"Basic Attack: {self.basic_attack}")
        print(f"Crit Rate: {self.crit_rate}")
        print(f"Crit Damage: {self.crit_dmg}")
        print(f"Attack Speed: {self.attack_speed}")
        print(f"Final Damage: {self.final_damage}")