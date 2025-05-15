import os, datetime

def logging(func):
    def log(*args, **kwargs):
        print(f'Имя функции: {func.__name__}')
        print(f'Документация к функции: {func.__doc__}')
        try:
            func(*args, **kwargs)
        except Exception as e:
            path_to_error_logs = os.path.abspath(__file__).replace('task3.py', 'function_errors.log')
            with open(path_to_error_logs, '+a', encoding='utf-8') as file:
                error = f'Функция {func.__name__} вызвала {e.__class__.__name__} в {datetime.datetime.now()}\n'
                file.write(error)
    return log

class Task3:
    @logging
    def main(self):
        """
        Main func
        """
        print('Main func working')
        raise ValueError

    @logging
    def main_second(self):
        """
        Second Main func
        """
        print('Second Main func working')
        raise NameError
    
    @logging
    def do_smth(self):
        """
        This func do somwething
        """
        print('do something')
        raise IndexError