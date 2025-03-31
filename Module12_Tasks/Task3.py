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

while True:
    try:
        user_number = int(input("Введите число: "))

        if(user_number >= 0):
            break

        print("Число должно быть больше 0")
    except:
        print("Это не число")


user_input = ""
while True:
    print("Введите номер действия: \n",
        "1 - сумма цифр \n",
        "2 - максимальная цифра \n",
        "3 - минимальная цифра")

    while True:
        try:
            user_input = input()
            if(user_input  == "exit"):
                break

            command = int(user_input)
            if(command >= 1 and command <= 3):
                break

            print("Введен неправильная команда")
        except:
            print("Это не число")

    if(user_input  == "exit"):
        break

    if (command == 1):
        print(f"Сумма цифр: {sum_0f_numbers(user_number)}")
    elif (command == 2):
        print(f"Максимальная цифра: {max_number(user_number)}")
    elif (command == 3):
        print(f"Минимальная цифра: {min_number(user_number)}") 