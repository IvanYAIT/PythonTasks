from services.user_input import call_until_valid_input

def sum_0f_numbers(number):
    result = 0
    for num in str(number):
        result += int(num)
    
    return result

def max_number(number):
    result = 0
    for num in str(number):
        if(int(num) > result):
            result = int(num)
    
    return result

def min_number(number):
    result = 10
    for num in str(number):
        if(int(num) < result):
            result = int(num)
    
    return result

@call_until_valid_input
def get_user_number():
    user_number = int(input("Введите число: "))

    if(user_number <= 0):
        raise ValueError
    
    return user_number

@call_until_valid_input
def get_command():
    user_input = input()
    if(user_input  == "exit"):
        return user_input

    command = int(user_input)
    if(command < 1 or command > 3):
        raise ValueError

    return command

user_number = get_user_number()
while True:
    print("Введите номер действия: \n",
        "1 - сумма цифр \n",
        "2 - максимальная цифра \n",
        "3 - минимальная цифра")

    command = get_command()
    if(str(command).lower() == "exit"):
        break

    if (command == 1):
        print(f"Сумма цифр: {sum_0f_numbers(user_number)}")
    elif (command == 2):
        print(f"Максимальная цифра: {max_number(user_number)}")
    elif (command == 3):
        print(f"Минимальная цифра: {min_number(user_number)}") 