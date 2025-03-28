def sum(number):
    result = 0
    for num in range(1, number+1):
        result += num
    
    return result

while True:
        try:
            userNumber = int(input("Введите число: "))

            if(userNumber > 0):
                break

            print("Число должно быть больше 0")
        except:
            print("Это не число")

print(f"Я знаю, что сумма чисел от 1 до {userNumber} равна {sum(userNumber)}")