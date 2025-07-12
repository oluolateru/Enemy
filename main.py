from App.Class.Zombie import *
from App.Class.Orge import *
from App.Class.Enemy import *
from App.Class.Hero import *
from App.Class.Weapon import *


def battle(e1: Enemy, e2: Enemy):
    print('--------------')
    e1.talk()
    e2.attack()
    e1.special_attach()
    e2.special_attach()

    while e1.health_points > 0 and e2.health_points > 0:
        print(f"{e1.get_type_of_enemy()}: has {e1.health_points} HP left.")
        print(f"{e2.get_type_of_enemy()}: has {e2.health_points} HP left.")
        e1.attack()
        e2.health_points -= e1.attack_damage
        e2.attack()
        e1.health_points -= e2.attack_damage
        print('--------------')


    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} wins!")
    else:
        print(f"{e2.get_type_of_enemy()} wins!")


def hero_battle(hero: Hero, enemy: Enemy):
    print('--------------')
    enemy.special_attach()

    while hero.health_points > 0 and enemy.health_points > 0:
        print(f"Hero: has {enemy.health_points} HP left.")
        print(f"{enemy.get_type_of_enemy()}: has {enemy.health_points} HP left.")
        hero.attack()
        enemy.health_points -= hero.attack_damage
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        print('--------------')


    if enemy.health_points > 0:
        print(f"{enemy.get_type_of_enemy()} wins!")
    else:
        print(f"Hero wins!")


zombie = Zombie()
orge = Orge(100, 3)

# battle(zombie, orge)

hero = Hero(10, 2)

weapon = Weapon('Sword', 100)

hero.weapon = weapon

hero.equip_weapon()

hero_battle(hero, orge)
# print (zombie.get_type_of_enemy())
#
# zombie.talk()
# # zombie.walk()
# # zombie.attack()
#
# print (orge.get_type_of_enemy())
# orge.attack()

#print(f"{enemy1.type_of_enemy} has health points {enemy1.health_points} and can do an attack damage of {enemy1.attack_damage}")