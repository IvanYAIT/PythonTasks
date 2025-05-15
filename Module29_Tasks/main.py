from Task1.task1 import User, PermissionType
from Task2.task2 import Task2
from Task3.task3 import Task3Child

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

#user_actions()
#check_callback_func()
print_logs()
