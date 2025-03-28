def SumOfNumbers(number):
    result = 0
    for num in str(number):
        result += int(num)
    
    return result

def MaxNumber(number):
    result = 0
    for num in str(number):
        if(int(num) > result):
            result = int(num)
    
    return result

def MinNumber(number):
    result = 10
    for num in str(number):
        if(int(num) < result):
            result = int(num)
    
    return result

while True:
    try:
        userNumber = int(input("Введите число: "))

        if(userNumber >= 0):
            break

        print("Число должно быть больше 0")
    except:
        print("Это не число")

print("Введите номер действия: \n",
        "1 - сумма цифр \n",
        "2 - максимальная цифра \n",
        "3 - минимальная цифра")

while True:
    try:
        userInput = int(input())

        if(userInput >= 1 and userInput <= 3):
            break

        print("Введен неправильная команда")
    except:
        print("Это не число")

if (userInput == 1):
    print(f"Сумма цифр: {SumOfNumbers(userNumber)}")
elif (userInput == 2):
    print(f"Максимальная цифра: {MaxNumber(userNumber)}")
elif (userInput == 3):
    print(f"Минимальная цифра: {MinNumber(userNumber)}") 