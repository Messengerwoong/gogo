import random
class Enemy:
        # type_of_enemy: str
        # health_points: int
        # attack_damage:int

        def __init__(self,type_of_enemy,health_points,attack_damage):
                self.__type_of_enemy = type_of_enemy
                self.attack_damage = attack_damage
                self.health_points = health_points
        def get_type_of_enemy(self):
                return self.__type_of_enemy
        def talk(self):
                print(f'I am a {self.__type_of_enemy}. Be prepare to flight!')

        def walk_forward(self):
                print(f'I am a {self.__type_of_enemy} move closer to you.')
        
        def attack(self):
                print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')

        def special_attack(self):
                did_special_attack_work = random.random() < 0.50
                if did_special_attack_work:
                        self.health_points +=2
                        print('Zombie regenerated 2 HP!')
                        

