from Enemy import *
from zombie import *
from orge import *
enemy = Enemy('Enemy',10,1)



zombie = Zombie(10,2)
orge = Ogre(30,2)

def battle(e1: Enemy, e2:Enemy):
    e1.special_attack()
    e2.special_attack()
    e2.attack()
    e1.special_attack()
    e1.health_points -= e2.attack_damage
    e1.attack()
    e2.special_attack()
    e1.special_attack()
    e2.health_points -= e1.attack_damage

    if e1.health_points >0:
        print("Enemy 1 wins!")
    else:
        print("Enemy 2 wins")
battle(zombie, orge)

