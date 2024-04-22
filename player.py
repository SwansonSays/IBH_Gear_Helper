class Player():
    def __init__(self, basic_attack, crit_rate, crit_dmg, attack_speed, final_damage) -> None:
        self.basic_attack = basic_attack
        self.crit_rate = crit_rate - 46.2
        self.crit_dmg = crit_dmg
        self.attack_speed = attack_speed + 100 - 252
        self.final_damage = final_damage
        