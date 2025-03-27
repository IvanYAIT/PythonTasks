while True:
    try:
        height = int(input("Введите высоту пирамиды: "))
        if(height > 0):
            break

        print("Число должно быть больше нуля")
    except:
        print("Это не число")

symbolsInRow = 1
for i in range(height-1, -1, -1):
    str = " " * i + "#" * symbolsInRow
    symbolsInRow += 2
    print(str)