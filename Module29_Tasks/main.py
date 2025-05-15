from Task1.task1 import User, PermissionType
from Task2.task2 import Task2
from Task3.task3 import Task3Child
from Task4.task4 import Task4
from Task5.task5 import Task5
from Task6.task6 import complex_algorithm

def user_actions():
    user = User()
    admin = User()
    user.set_permission(PermissionType.USER)
    admin.set_permission(PermissionType.ADMIN)

    user.add_comment('user')
    admin.add_comment('admin')

    admin.delete_site()
    user.delete_site()

def check_callback_func():
    Task2.main()

def print_logs():
    task3 = Task3Child()
    task3.test_func1()
    task3.test_func2()

def decorate_the_world():
    task4 = Task4()
    task4.decorated_func('User', 101)

def check_singelton():
    task5 = Task5()
    another_task5 = Task5()
    print(id(task5))
    print(id(another_task5))
    print(task5 is another_task5)

def check_class_decorator():
    complex_algorithm(10, 50)

#user_actions()
#check_callback_func()
#print_logs()
#decorate_the_world()
#check_singelton()
check_class_decorator()
