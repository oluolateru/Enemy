from App.Class.Enemy import *
import random

class Orge(Enemy):
    def __init__(self, health_points = 10, attack_damage = 1):
        super().__init__(type_of_enemy='Orge',
                         health_points = health_points,
                         attack_damage = attack_damage
                         )

    def talk(self):
        print(f"I am {self.get_type_of_enemy()} and I am slamming my hands on the floor!.")

    def special_attach(self):
        did_special_attack_happen = random.random() < 0.2
        if did_special_attack_happen:
            self.attack_damage = 4
            print(f"{self.get_type_of_enemy()}: get angry and increase attack damage to 4!")