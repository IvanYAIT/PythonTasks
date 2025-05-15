from Task1.task1 import Task1
from Task2.task2 import MyMath
from Task3.task3 import Date
from Task4.task4 import LRU_Cache

def write_to_file():
    path = 'C:\\Users\\Якушик И_А\\Documents\\work\\PythonTasks\\Module28_Tasks\\Task1\\file.txt'
    task1 = Task1()
    task1.open_file(path)

def math_class():
    math = MyMath()
    lenght = math.count_lenght_of_circle(3)
    circle_area = math.count_area_of_circle(5)
    sphere_surface_area = math.count_area_of_sphere_surface(4)
    cube_volume = math.count_volume_of_cube(3)
    print(f'{lenght} {circle_area} {sphere_surface_area} {cube_volume}')

def print_date():
    date = Date.from_string('20-03-2056')
    print(date)
    print(Date.is_valid('14-11-1045'))
    print(Date.is_valid('23-13-2077'))

def print_cached_data():
    cache = LRU_Cache()
    cache.cache = ('key1', 'value1')
    cache.cache = ('key2', 'value2')
    cache.cache = ('key3', 'value3')
    print(cache.get('key2'))
    cache.cache = ('key4', 'value4')
    print(cache)

#write_to_file()
#math_class()
#print_date()
print_cached_data()
