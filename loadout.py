class Loadout():
    def __init__(self, player, items) -> None:
        self.basic_attack = player.basic_attack
        self.crit_rate = player.crit_rate
        self.crit_dmg = player.crit_dmg
        self.attack_speed = player.attack_speed
        self.final_damage = player.final_damage
        self.super_crit_rate = player.super_crit_rate
        self.super_crit_dmg = player.super_crit_dmg
        self.items = items


        #combine player stats with item stats for full loadout stats
        for item in items:
            self.basic_attack += item.basic_attack
            self.crit_rate += item.crit_rate
            self.crit_dmg += item.crit_dmg
            self.attack_speed += item.attack_speed
            self.final_damage += item.final_damage

        self.super_crit_actual_dmg = self.super_crit_dmg * self.crit_dmg / 100 #supercrit dmg calculation

        self.calculate_stats()


    def calculate_stats(self):
        #Damage formula from spreadsheet
        crit_ratio = min(self.crit_rate, 100) * (100 - self.super_crit_rate) / 100
        super_crit_ratio = min(self.crit_rate, 100) * self.super_crit_rate / 100
        hit_ratio = 100 - crit_ratio - super_crit_ratio

        base_dmg = self.basic_attack * (self.final_damage / 100) * 1.25
        damage_crit = self.crit_dmg / 100 * base_dmg
        damage_super_crit = self.super_crit_actual_dmg / 100 * base_dmg

        self.total_dmg = (damage_crit * crit_ratio / 100) + (damage_super_crit * super_crit_ratio / 100) + (base_dmg * hit_ratio / 100)

        self.combat_power = min(self.attack_speed, 400) / 100 * self.total_dmg


    def print(self, verbose: int) -> None:
        print("\n*****************************")
        print("*      -LOADOUT STATS-      *")
        print(f"* Basic Attack: {round(self.basic_attack, 2)}   *")
        print(f"* Crit Rate: {round(self.crit_rate, 2)}         *")
        print(f"* Crit Damage: {round(self.crit_dmg, 2)}      *")
        print(f"* Attack Speed: {round(self.attack_speed, 2)}      *")
        print(f"* Final Damage: {round(self.final_damage, 2)}     *")
        print(f"* Super Crit Rate: {round(self.super_crit_rate, 2)}    *")
        print(f"* Super Crit Damage: {round(self.super_crit_dmg, 2)}  *")
        print("*****************************")
        print(f"Total Damage: {round(self.total_dmg, 2)}")
        print(f"Total Damage: {round(self.total_dmg / 1000, 2)}a") 
        print(f"Total Damage: {round(self.total_dmg / 1000000, 2)}b") 
        print(f"Total Damage: {round(self.total_dmg / 1000000000, 2)}c") 
        print()
        print(f"Combat Power: {round(self.combat_power, 2)}")
        print(f"Combat Power: {round(self.combat_power / 1000, 2)}a") 
        print(f"Combat Power: {round(self.combat_power / 1000000, 2)}b") 
        print(f"Combat Power: {round(self.combat_power / 1000000000, 2)}c") 

        if(verbose == 1):
            for item in self.items:
                item.print(1)


    
        