while True:
    try:
        number = float(input("Введите число: "))

        if(number > 0):
            break

        print("Число должно быть больше 0")
    except:
        print("Это не число")

power_index = 0
if(number >= 1):
    power_index = ((len(str(number))-3)* -1)
    result = number * 10 ** power_index
else:
    power_index = (len(str(number%1))-3)
    result = number * 10 ** power_index

print(f"Формат плавающей точки: {result} * 10 ** {power_index * -1}")