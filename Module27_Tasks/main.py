from Task1.task1 import Task1
from Task2.task2 import Task2
from Task3.task3 import Task3

def test_decorator():
    task1 = Task1()
    task1.main()

def test_delayed_func():
    task2 = Task2()
    task2.main()

def tes_logging_decorator():
    task3 = Task3()
    task3.main()
    task3.main_second()
    task3.do_smth()

#test_decorator()
#test_delayed_func()
tes_logging_decorator()
