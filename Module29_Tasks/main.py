from Task1.task1 import User, PermissionType

def user_actions():
    user = User()
    admin = User()
    user.set_permission(PermissionType.USER)
    admin.set_permission(PermissionType.ADMIN)

    user.add_comment('user')
    admin.add_comment('admin')

    admin.delete_site()
    user.delete_site()

user_actions()
