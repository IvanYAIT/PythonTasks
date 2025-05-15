from time import sleep

def wait_for_seconds(seconds : int):
    def delay_func(func):
        def wait(*args, **kwargs):
            sleep(seconds)
            func(*args, **kwargs)
        return wait
    return delay_func

class Task2:
    @wait_for_seconds(2)
    def main(self):
        print('Эта функция замедлена')
