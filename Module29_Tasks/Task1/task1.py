import enum

class PermissionType(enum.Enum):
    ADMIN = 0
    USER = 1

def check_permission(permission : PermissionType):
    def get_permission(func):
        def check(*args, **kwargs):
            if permission == PermissionType.ADMIN:
                if permission == args[0].get_permission():
                    func(*args, **kwargs)
                else:
                    raise PermissionError
            else:
                func(*args, **kwargs)
        return check
    return get_permission

class User:
    __permission_type = None

    def get_permission(self):
        return self.__permission_type

    def set_permission(self, permission : PermissionType):
        self.__permission_type = permission

    @check_permission(PermissionType.ADMIN)
    def delete_site(self):
        print('Сайт удален')
    
    @check_permission(PermissionType.USER)
    def add_comment(self, comment : str):
        print(f'Добавлен комментарий: {comment}')
