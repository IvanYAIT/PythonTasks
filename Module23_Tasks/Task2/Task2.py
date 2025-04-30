import random, os
from services.user_input import call_until_valid_input

class Task2:
    PATH_TO_FILE = os.path.abspath(__file__).replace('Task2.py', 'out_file.txt')

    @call_until_valid_input
    def get_user_number(self):
        return int(input('Введите число: '))

    def try_your_luck(self):
        if random.randint(1, 13) == 1:
            raise Exception('Вас постигла неудача!')
        
    def count_lucky_number(self):
        lucky_number = 0
        with open(self.PATH_TO_FILE, '+w') as file:
            while lucky_number < 777:
                number = self.get_user_number()
                self.try_your_luck()
                file.write(str(number)+'\n')
                lucky_number += number
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    
    def main(self):
        self.count_lucky_number()