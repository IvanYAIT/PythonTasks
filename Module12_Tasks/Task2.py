from services.user_input import call_until_valid_input

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

@call_until_valid_input
def get_user_number():
    return int(input("Введите число: "))

def test():
    user_number = get_user_number()
    
    if(user_number >= 0):
        positive()
    else:
        negative()

test()