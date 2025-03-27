start = None
end = None

while True:
    try:
        if (start is None):
            start = int(input("Введите начало отрезка: "))
        
        if (end is None):
            end = int(input("Введите конец отрезка: "))
        
        step = int(input("Введите шаг: "))
        if(step > 0):
            step *= -1

        if(step < 0):
            break

        print("Шаг не может быть нулем")
    except:
        print("Какие-то данные веден не правильно")

if(start > end):
    for point in range(start, end-1, step):
        result = point ** 3 + 2 * point ** 2 - 4 * point + 1
        print(f"В точке {point} функция равна {result}")
elif (start < end):
    for point in range(end, start-1, step):
        result = point ** 3 + 2 * point ** 2 - 4 * point + 1
        print(f"В точке {point} функция равна {result}")