def counter(func):
    def count(*args, **kwargs):
        count.amount += 1
        return func(*args, **kwargs)
    count.amount = 0
    return count

class Task5:
    @counter
    def main(self):
        print('main')
    