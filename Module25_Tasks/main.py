from Task1.Task1 import Car, Appartment, CountryHouse
from Task2.Task2 import KarmaCollector
from Task3.Task3 import My_Dict
from Task4.Task4 import TaskManager
from Task5.Task5 import Circle, Triangle, Rectangle

def count_taxes():
    car = Car(5_000_000)
    appartment = Appartment(12_500_000)
    country_house = CountryHouse(45_300_000)

    overall_tax = car.count_tax() + appartment.count_tax() + country_house.count_tax()
    print(f'Итого налогов: {overall_tax}')

def collect_karma():
    karma_collector = KarmaCollector()
    while karma_collector.current_karma < karma_collector.MAX_KARMA:
        karma_collector.one_day()
    print(f'Накопилось {karma_collector.current_karma} кармы')

def print_my_dict():
    my_dict = My_Dict()
    my_dict['1'] = 1
    my_dict['2'] = 2
    my_dict['3'] = 3
    print(my_dict.get('1'))
    print(my_dict.get('4'))

def print_task_list():
    manager = TaskManager()
    manager.new_task('Sleep', 1)
    manager.new_task('Work', 3)
    manager.new_task('Eat', 2)
    manager.new_task('Play', 2)

    manager.print_tasks()

def print_areas():
    rectangle = Rectangle(2, 3)
    circle = Circle(5)
    triangle = Triangle(3, 3, 2)

    print(f'Площадь прямоугольника: {rectangle.area()}')
    print(f'Площадь круга: {circle.area()}')
    print(f'Площадь треугольника: {triangle.area()}')
    
#count_taxes()
#collect_karma()
#print_my_dict()
#print_task_list()
print_areas()