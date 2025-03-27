while True:
    try:
        a = int(input("Введите начало отрезка: "))
    except:
        print("Это не число")
    else:
        break

while True:
    try:
        b = int(input("Введите конец отрезка: "))
    except:
        print("Это не число")
    else:
        break

numberSum = 0
numberCount = 0
print("Числа из отрезка, которые делятся на 3:")
for number in  range(a, b+1):
    if(number % 3 == 0):
        print(number)
        numberSum += number
        numberCount += 1

print(f"Среднее арифметическое этих чисел: {numberSum/numberCount:.1f}")