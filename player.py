class Player():
    #set player stats with base modifiers
    def __init__(self, basic_attack, crit_rate, crit_dmg, attack_speed, final_damage, super_crit_rate, super_crit_dmg) -> None:
        self.basic_attack = basic_attack
        self.crit_rate = crit_rate
        self.crit_dmg = crit_dmg + 100
        self.attack_speed = attack_speed + 100
        self.final_damage = final_damage + 100
        self.super_crit_rate = super_crit_rate
        self.super_crit_dmg = super_crit_dmg + 100
