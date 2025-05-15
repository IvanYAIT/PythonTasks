def decorator_with_args_for_any_decorator(decorator):
    def wrapper(*args, **kwargs) :
        def inner(func):
            return decorator(func, *args, **kwargs)
        return inner
    return wrapper

@decorator_with_args_for_any_decorator
def decorated_decorator(func, *args, **kwargs):
    def wrapper(*args_wrap, **kwargs_wrap):
        print(f"Переданные арги и кварги в декоратор: {args}, {kwargs}")
        return func(*args_wrap, **kwargs_wrap)
    return wrapper


class Task4:
    @decorated_decorator(100, 'рублей', 200, 'друзей')
    def decorated_func(self, name :str, num : int):
        print(f'привет {name} {num}')
