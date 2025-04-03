import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '../Services'))

from UserInput import *

@check_input
def get_user_number():
    user_number = int(input("Введите число: "))

    if(user_number <= 0):
        raise ValueError
    
    return user_number

def sum_to_number(number):
    result = 0
    for num in range(1, number+1):
        result += num
    
    return result

user_number = get_user_number()
print(f"Я знаю, что сумма чисел от 1 до {user_number} равна {sum_to_number(user_number)}")