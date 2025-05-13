from Task1.task1 import Task1
from Task2.task2 import Task2

def test_decorator():
    task1 = Task1()
    task1.main()

def test_delayed_func():
    task2 = Task2()
    task2.main()

#test_decorator()
test_delayed_func()
