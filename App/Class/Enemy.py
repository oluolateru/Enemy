class Enemy:

    def __init__(self, type_of_enemy, health_points = 10, attack_damage = 1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage



    def talk(self):
        print(f"I am {self.get_type_of_enemy()}, get ready to fight")

    def walk(self):
        print(f"Enemy {self.get_type_of_enemy()} is moving closer to you.")

    def attack(self):
        print(f"Enemy {self.get_type_of_enemy()} attack you with damage of {self.attack_damage}.")

    def get_type_of_enemy(self):
        return self.__type_of_enemy