from App.Class.Zombie import *
from App.Class.Orge import *

zombie = Zombie()

orge = Orge(100, 3)

print (zombie.get_type_of_enemy())

zombie.talk()
# zombie.walk()
# zombie.attack()

print (orge.get_type_of_enemy())
orge.attack()

#print(f"{enemy1.type_of_enemy} has health points {enemy1.health_points} and can do an attack damage of {enemy1.attack_damage}")