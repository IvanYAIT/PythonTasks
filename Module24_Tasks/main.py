from Task1.Task1 import Warrior, Arena

warrior1 = Warrior(100, 15)
warrior2 = Warrior(100, 15)
warrior3 = Warrior(50, 30)
warrior4 = Warrior(150, 5)

arena = Arena(warrior1, warrior2, warrior3, warrior4)
arena.battle()