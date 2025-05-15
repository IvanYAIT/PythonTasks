import time

class LoggerDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwds):
        start = time.time()
        result = self.function(*args, **kwds)
        end = time.time()
        print(f'Вызов функции {self.function.__name__}')
        print(f'Аргументы: {args} {kwds}')
        print(f'Результат: {result}')
        print(f'Время выполнения: {round(end - start, 4)} секунд')

@LoggerDecorator
def complex_algorithm(arg1, arg2):
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('Module29_Tasks\\Task6\\test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result