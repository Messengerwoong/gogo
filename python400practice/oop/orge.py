from Enemy import * 
class Ogre(Enemy):
        def __init__(self, health_points, attack_damage):
                super().__init__(type_of_enemy='Orge', health_points=health_points, attack_damage=attack_damage)
        def talk(self):
            print('Ogre is slamming hands all around')
        def spread_disease(self):
            print('The Zombie is trying to spread infection')
        def special_attack(self):
                did_special_attack_work = random.random() < 0.20
                if did_special_attack_work:
                        self.attack_damage +=4
                        print('Orge attack has increased by 4!')

                        
