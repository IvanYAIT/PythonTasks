import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '../Services'))

from UserInput import *

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

@check_input
def get_user_number():
    return int(input("Введите число: "))

def test():
    user_number = get_user_number()
    
    if(user_number >= 0):
        positive()
    else:
        negative()

test()