from monsters import MonsterBerserk, MonsterHunter
 
class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние
 
    max_hp = 150
    start_power = 10
 
    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True
 
    def get_hp(self):
        return self.__hp
 
    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)
 
    def get_power(self):
        return self.__power
 
    def set_power(self, new_power):
        self.__power = new_power
 
    def is_alive(self):
        return self.__is_alive
 
    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        pass
 
    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False
 
    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)
 
    def __str__(self):
        pass
 
 
class Healer(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.__mag_power = self.get_power() * 3

    def attack(self, target):
        target.take_damage(self.get_power() / 2)
        print(f'{self.name} атакует {target.name} на {round(self.get_power() / 2, 2)}')

    def receive_damage(self, damage):
        super().take_damage(damage * 1.2)
        print(f'{self.name} получает {damage * 1.2} урона, осталось здоровья {self.get_hp()}')

    def heal(self, target):
        target.set_hp(target.get_hp() + self.__mag_power)
        print(f'{self.name} лечит {target.name} на {self.__mag_power}')

    def find_weakest_ally(self, allies):
        weakest = None
        for ally in allies:
            if ally.max_hp == ally.get_hp():
                continue
            if weakest:
                if weakest.get_hp() > ally.get_hp():
                    weakest = ally
                    continue
            else:
                weakest = ally
        return weakest
    
    def find_strongest_enemy(self, enemies):
        strongest = enemies[0]
        for enemy in enemies:
            if strongest.get_hp() > enemy.get_hp():
                strongest = enemy
        return strongest
    
    def choose_action(self, allies, enemies):
        if self.get_hp() <= 0:
            return
        target = self.find_weakest_ally(allies)
        if target:
            self.heal(target)
        else:
            target = self.find_strongest_enemy(enemies)
            if target:
                self.attack(target)
    
    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        self.choose_action(friends, enemies)
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель
 
 
class Tank(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.__defense = 1
        self.__is_shield_up = False
 
    def attack(self, target):
        damage = self.get_power() / 2
        target.take_damage(damage)
        print(f'{self.name} атакует {target.name} на {round(damage, 2)}')

    def receive_damage(self, damage):
        damage /= self.__defense
        super().take_damage(damage)
        print(f'{self.name} получает {damage} урона, осталось здоровья {self.get_hp()}')

    def raise_shield(self):
        if not self.__is_shield_up:
            self.__is_shield_up = True
            self.set_power(self.get_power() / 2) 
            self.__defense *= 2
            print(f'{self.name} поднял щит')

    def lower_shield(self):
        if self.__is_shield_up:
            self.__is_shield_up = False
            self.set_power(self.get_power() * 2) 
            self.__defense /= 2
            print(f'{self.name} опустил щит')

    def find_closest_enemy(self, enemies):
        closest = enemies[0]
        for enemy in enemies:
            if isinstance(enemy, MonsterBerserk):
                closest = enemy
                return closest
        return closest
    
    def choose_action(self, allies, enemies):
        if self.get_hp() <= 0:
            return
        if self.__is_shield_up:
            self.lower_shield()
        else:
            target = self.find_closest_enemy(enemies)
            if target:
                self.attack(target)
            else:
                self.raise_shield()
    
    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        self.choose_action(friends, enemies)
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель
 
class Attacker(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.__power_multiply = 2
        self.is_powered = False
 
    def attack(self, target):
        damage = self.get_power() * self.__power_multiply
        target.take_damage(damage)
        self.power_down()
        print(f'{self.name} атакует {target.name} на {round(damage, 2)}')

    def receive_damage(self, damage):
        damage *= self.__power_multiply / 2
        super().take_damage(damage)
        print(f'{self.name} получает {damage} урона, осталось здоровья {self.get_hp()}')

    def power_up(self):
        self.__power_multiply *= 2
        self.is_powered = True
        print(f'{self.name} усилился')

    def power_down(self):
        self.__power_multiply /= 2
        self.is_powered = False
        print(f'{self.name} ослабился')

    def find_weakest_enemy(self, enemies):
        weakest = enemies[0]
        for enemy in enemies:
            if isinstance(enemy, MonsterHunter):
                weakest = enemy
                return weakest
            if weakest.get_hp() > enemy.get_hp():
                weakest = enemy
        return weakest
    
    def choose_action(self, allies, enemies):
        if self.get_hp() <= 0:
            return
        
        if not self.is_powered:
            self.power_up()
            return
        
        target = self.find_weakest_enemy(enemies)
        if target:
            self.attack(target)

    def make_a_move(self, friends, enemies):
        super().make_a_move(friends, enemies)
        self.choose_action(friends, enemies)
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
