def count_numbers(number):
    return len(str(number))

def change_number(number):
    result = ""
    numsOfNumber = list(str(number))
    firstNum = numsOfNumber[0]
    numsOfNumber[0] = numsOfNumber[count_numbers(number)-1]
    numsOfNumber[count_numbers(number)-1] = firstNum
    result = ''.join(numsOfNumber)
    return int(result)

def main():
    firstNumber = None
    secondNumber = None

    while True:
        try:
            if(firstNumber is None):
                firstNumber = int(input("Введите первое число: "))

            if(len(str(firstNumber)) < 3 or firstNumber < 0):
                print("Первое число должно быть трехзначным или больше")
                firstNumber = None
                continue

            if(secondNumber is None):
                secondNumber = int(input("Введите второе число: "))

            if(len(str(secondNumber)) < 4 or secondNumber < 0):
                print("Второе число должно быть четырехзначное или больше")
                secondNumber = None
                continue

            userNumbers = [firstNumber, secondNumber]
            break
        except:
            print("Это не число")
    
    for index in range(len(userNumbers)):
        userNumbers[index] = change_number(userNumbers[index])

    print(f"Сумма чисел равна: {userNumbers[0] + userNumbers[1]}")

main()