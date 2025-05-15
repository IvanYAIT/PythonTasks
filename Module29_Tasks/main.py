from Task1.task1 import User, PermissionType
from Task2.task2 import Task2

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

#user_actions()
check_callback_func()
