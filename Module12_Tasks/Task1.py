from services.user_input import call_until_valid_input

@call_until_valid_input
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