
app = {}

def callback(route : str):
    def call(func):
        app[route] = func
    return call

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

class Task2:
    @classmethod
    def main(cls):
        route = app.get('//')
        if route:
            status = route()
            print(f'Статус: {status}')
        else:
            print('Нет такого пути')
