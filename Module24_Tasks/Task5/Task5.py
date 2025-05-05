import random

class House:
    food = 50
    money = 0

class Human:
    satiety = 50

    def __init__(self, name, house : House):
        self.name = name
        self.house = house
    
    def eat(self, satiety_per_food = 10, food_per_eat = 5):
        if self.house.food >= food_per_eat:
            self.satiety += satiety_per_food
            self.house.food -= food_per_eat
            return True
        return False
    
    def work(self, money_per_work = 20, satiety_per_work = 15):
        if self.satiety >= satiety_per_work:
            self.house.money += money_per_work
            self.satiety -= satiety_per_work
            return True
        return False
    
    def go_to_mall(self, money_per_shopping = 15, food_per_shopping = 10):
        if self.house.money >= money_per_shopping:
            self.house.food += food_per_shopping
            self.house.money -= money_per_shopping
            return True
        return False
    
    def play(self, satiety_per_playing = 5):
        if self.satiety >= satiety_per_playing:
            self.satiety -= satiety_per_playing
            return True
        return False

    def death(self):
        return self.satiety <= 0

class Challenge:


    def __init__(self, human : Human):
        self.human = human
        self.house = human.house
    
    def roll_a_dice(self):
        number = random.randint(1, 6)
        if number == 1:
            self.human.work()
        elif number == 2:
            self.human.play()

    def start(self):
        days = 0
        while days != 365:
            if self.human.satiety < 20:
                self.roll_a_dice() if self.human.eat() else None
            elif self.house.food < 10:
                self.roll_a_dice if self.human.go_to_mall() else None
            elif self.house.money < 50:
                self.roll_a_dice if self.human.work() else None
            else:
                self.roll_a_dice
            
            if self.human.death():
                print(f'{self.human.name} умер( Прожил: {days}д')
                return
            
            days += 1
        print(f'{self.human.name} прожил все {days}д. Осталось {self.house.money} руб и {self.house.food} еды')
                