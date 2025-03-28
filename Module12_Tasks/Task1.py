while True:
    try:
        number = float(input("Введите число: "))

        if(number > 0):
            break

        print("Число должно быть больше 0")
    except:
        print("Это не число")

powerIndex = 0
if(number >= 1):
    powerIndex = ((len(str(number))-3)* -1)
    result = number * 10 ** powerIndex
else:
    powerIndex = (len(str(number%1))-3)
    result = number * 10 ** powerIndex

print(f"Формат плавающей точки: {result} * 10 ** {powerIndex * -1}")