import random

class Warrior:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    
    def get_damage(self, damage):
        self.health -= damage

class Arena:
    def __init__(self, *args):
        self.warriors = list(args)

    def battle(self):
        while True:
            first_warrior_index = random.randint(0, len(self.warriors)-1)
            second_warrior_index = random.randint(0, len(self.warriors)-1)

            if(first_warrior_index == second_warrior_index):
                continue

            self.warriors[second_warrior_index].get_damage(self.warriors[first_warrior_index].damage)
            print(f"Воин {first_warrior_index+1} нанес {self.warriors[first_warrior_index].damage} войну {second_warrior_index+1}")

            if(self.warriors[second_warrior_index].health <= 0):
                self.warriors.remove(self.warriors[second_warrior_index])
            
            if(len(self.warriors) == 1):
                print('Остался один воин')
                return