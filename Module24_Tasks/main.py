from Task1.Task1 import Warrior, Arena
from Task2.Task2 import Student
from Task3.Task3 import Child, Parent
from Task4.Task4 import *

def print_warriors_fight():
    warrior1 = Warrior(100, 15)
    warrior2 = Warrior(100, 15)
    warrior3 = Warrior(50, 30)
    warrior4 = Warrior(150, 5)

    arena = Arena(warrior1, warrior2, warrior3, warrior4)
    arena.battle()

def print_students():
    student1 = Student('Мальцева Софья', 2, [3, 4, 4, 5, 2])
    student2 = Student('Голубева София', 1, [6, 4, 3, 5, 4])
    student3 = Student('Кондратьев Тимофей', 2, [3, 3, 2, 5, 4])
    student4 = Student('Владимиров Роман', 3, [4, 4, 5, 5, 2])
    student5 = Student('Кошелев Пётр', 3, [5, 5, 4, 5, 2])
    student6 = Student('Кузнецова Вера', 1, [2, 4, 2, 5, 2])
    student7 = Student('Никитин Лев', 3, [3, 3, 4, 5, 3])
    student8 = Student('Широков Дмитрий', 2, [5, 5, 5, 5, 5])
    student9 = Student('Владимирова Альбина', 1, [4, 4, 4, 4, 4])
    student10 = Student('Евдокимова Алиса', 1, [4, 4, 4, 5, 4])

    students = []
    students.append(student1)
    students.append(student2)
    students.append(student3)
    students.append(student4)
    students.append(student5)
    students.append(student6)
    students.append(student7)
    students.append(student8)
    students.append(student9)
    students.append(student10)

    students = sorted(students, key=lambda item: item.get_average_mark())
    for student in students:
        print(f"Студент {student.full_name}, средняя оценка: {student.get_average_mark()}")

def print_parents_info():
    child1 = Child('Ivan', 5)
    child2 = Child('Sasha', 11)
    child3 = Child('Kirill', 8)
    parent1 = Parent('Igor', 32, child1)
    parent2 = Parent('Daria', 42, child2, child3)

    parent1.get_info()
    parent1.feed_childrens()
    parent1.calm_childrens()
    parent2.get_info()
    parent2.feed_childrens()
    parent2.calm_childrens()
    parent1.feed_childrens()
    parent2.calm_childrens()

def print_elements():
    fire = Fire()
    water = Water()
    air = Air()
    earth = Earth()

    element1 = fire + water
    element2 = air + water
    element3 = earth + air
    element4 = fire + element1

    print(element1.element_type.name)
    print(element2.element_type.name)
    print(element3.element_type.name)
    print(element4.element_type.name)

#print_warriors_fight()
#print_students()
#print_parents_info()
print_elements()