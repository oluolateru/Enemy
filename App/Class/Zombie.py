from App.Class.Enemy import *
import random

class Zombie(Enemy):

    def __init__(self, health_points = 10, attack_damage = 1):
        super().__init__(type_of_enemy='Zombie',
                         health_points = health_points,
                         attack_damage = attack_damage
                         )

    def talk(self):
        print(f"I am {self.get_type_of_enemy()} and I am talking.")

    def spread_disease(self):
        print(f"{self.get_type_of_enemy()} is spreading disease!")

    def special_attach(self):
        did_special_attack_happen = random.random() < 0.5
        if did_special_attack_happen:
            self.health_points += 2
            print(f"{self.get_type_of_enemy()}: gain 2 HP!")