def sum(number):
    result = 0
    for num in range(1, number+1):
        result += num
    
    return result

while True:
        try:
            user_number = int(input("Введите число: "))

            if(user_number > 0):
                break

            print("Число должно быть больше 0")
        except:
            print("Это не число")

print(f"Я знаю, что сумма чисел от 1 до {user_number} равна {sum(user_number)}")