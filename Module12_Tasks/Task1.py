import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '../Services'))

from UserInput import *

def sum_to_number(number):
    result = 0
    for num in range(1, number+1):
        result += num
    
    return result

user_number = get_user_positive_number("int")
print(f"Я знаю, что сумма чисел от 1 до {user_number} равна {sum_to_number(user_number)}")