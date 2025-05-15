import functools 
from datetime import datetime 
import time 

def timer(cls, func, date_format): 
    @functools.wraps(cls) 
    def wrapped(*args, **kwargs): 
        format = date_format 
        for sym in format: 
            if sym.isalpha(): 
                format = format.replace(sym, '%' + sym) 
        print(f'Запускается {cls.__name__}.{func.__name__} Дата и время запуска: {datetime.now().strftime(format)}') 
        start = time.time() 
        result = func(*args, **kwargs) 
        end = time.time() 
        print(f'\nЗавершение {cls.__name__}.{func.__name__}, время работы = {round(end - start, 4)} сек.') 
        return result 
    return wrapped 

def log_methods(date_format): 
    def decorate(cls): 
        for method in dir(cls): 
            if not method.startswith('__'): 
                current_method = getattr(cls, method) 
                decorated_method = timer(cls, current_method, date_format) 
                setattr(cls, method, decorated_method) 
        return cls 
    return decorate 


@log_methods("b d Y - H:M:S")
class Task3:
    def test_func1(self):
        print("test func 1")
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class Task3Child(Task3):
    def test_func1(self):
        result = super().test_func1()
        print('Наследник от Task3')
        return result
    
    def test_func2(self):
        print("test func 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result