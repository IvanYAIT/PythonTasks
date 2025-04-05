import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '../Services'))

from UserInput import *

class Task3:
    @check_input
    def get_user_number():
        user_number = int(input("Введите число: "))

        if(user_number <= 0):
            raise ValueError
    
        return user_number

    def find_min_divider(number):
        if (number % 2 == 0): 
            return 2
        result = 3
        while (number % result != 0 and result * result <= number):
            result+= 2
        if (result * result <= number): 
            return result
        return number
    
    @classmethod
    def main(cls):
        number = cls.get_user_number()
        divider = cls.find_min_divider(number)
        print(f"Наименьший делитель, отличный от единицы: {divider}")
