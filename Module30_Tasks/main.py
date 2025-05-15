from Task1.task1 import Task1
from Task2.task2 import Task2
from Task3.task3 import Task3

def check_task2():
    task2 = Task2()
    task2.main()

def check_polindroms():
    task3 = Task3()
    print(task3.can_be_poly('ababc'))
    print(task3.can_be_poly('abbbc'))

#Task1.main()
#check_task2()
check_polindroms()
