import math

from services.user_input import call_until_valid_input

class Task5:
    @call_until_valid_input
    def get_number():
        number = int(input("Введите число: "))

        if number <= 0:
            raise ValueError('Число не может быть меньше нуля')
        
        return number
    
    def count_square_root(number):
        return round(math.sqrt(number), 3)
    
    @classmethod
    def main(cls):
        number = cls.get_number()
        num_square = cls.count_square_root(number)
        print(f'Квадрат числа {number}: {num_square}')