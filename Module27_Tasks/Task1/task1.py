def how_are_you(func):
    def question(*args, **kwargs):
        input('Как дела? ')
        print('А у меня не очень')
        func(*args, **kwargs)
    return question

class Task1:
    @how_are_you
    def main(self):
        print('Работа главной функции')