from Task1.task1 import Task1
from Task2.task2 import MyMath

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

#write_to_file()
math_class()
