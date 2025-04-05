import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '../Services'))

from UserInput import *

class Task2:
    @check_input
    def get_user_number():
        user_number = int(input("Введите число: "))

        if(user_number <= 0):
            raise ValueError
    
        return user_number
    
    def sum_of_number(number):
        result = 0
        for num in str(number):
            result += int(num)

        print(f"Сумма цифр: {result}")
        return result
    
    def count_nums_in_number(number):
        result = len(str(number))
        print(f"Кол-во цифр в числе: {result}")
        return result
    
    @classmethod
    def main(cls):
        number = cls.get_user_number()
        sum_of_number = cls.sum_of_number(number)
        amount_of_number = cls.count_nums_in_number(number)
        print(f"Разность суммы и кол-ва цифр: {sum_of_number - amount_of_number}")