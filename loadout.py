class Loadout():
    def __init__(self, player, items) -> None:
        self.basic_attack = player.basic_attack
        self.crit_rate = player.crit_rate
        self.crit_dmg = player.crit_dmg
        self.attack_speed = player.attack_speed
        self.final_damage = player.final_damage

        for item in items:
            self.basic_attack += item.basic_attack
            self.crit_rate += item.crit_rate
            self.crit_dmg += item.crit_dmg
            self.attack_speed += item.attack_speed
            self.final_damage += item.final_damage


    def print(self) -> None:
        print(f"Basic Attack: {self.basic_attack}")
        print(f"Crit Rate: {self.crit_rate}")
        print(f"Crit Damage: {self.crit_dmg}")
        print(f"Attack Speed: {self.attack_speed}")
        print(f"Final Damage: {self.final_damage}")
        