from Task1.task1 import Task1
from Task2.task2 import Task2
from Task3.task3 import Task3
from Task4.task4 import Task4
from Task5.task5 import Task5

def test_decorator():
    task1 = Task1()
    task1.main()

def test_delayed_func():
    task2 = Task2()
    task2.main()

def test_logging_decorator():
    task3 = Task3()
    task3.main()
    task3.main_second()
    task3.do_smth()

def count_fibanachi_number():
    task4 = Task4()
    number1 = task4.fib(6)
    number2 = task4.fib(6)
    number3 = task4.fib(6)
    print(number1)
    print(number2)
    print(number3)

def count_calls():
    task5 = Task5()
    task5.main()
    task5.main()
    task5.main()
    task5.main()

#test_decorator()
#test_delayed_func()
#test_logging_decorator()
#count_fibanachi_number()
count_calls()
