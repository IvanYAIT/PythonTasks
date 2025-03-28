while True:
    try:
        numCount = float(input("Введите число: "))

        if(numCount >= 0):
            break
        
        print("Чисел должна быть больше 0")
    except:
        print("Это не число")

result = int((numCount*10) // 1 - (numCount//1) * 10) 
print(f"Первое цифра после десятичной точки: {result}")

#int((numCount % 1) * 10) это способ работает, но если целая чсть числа будет 1 то он отдаст странные остаток. Пример если делить 1.2 на 1 остаток равен 0.1999996