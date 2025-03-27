rows = None
seats = None
gap = None

while True:
    try:
        if(rows is None):
            rows = int(input("Введите кол-во рядов: "))
        
        if(rows <= 0):
            rows = None
            print("Рядов не может быть меньше или равно нулю")
            continue

        if(seats is None):
            seats = int(input("Введите кол-во сидений ряду: "))
        
        if(seats <= 0):
            seats = None
            print("Сидений не может быть меньше или равно нулю")
            continue

        if(gap is None):
            gap = int(input("Введите кол-во метров между рядами: "))

        if(gap < 0):
            gap = None
            print("Пропуск между рядами не может быть меньше нуля")
            continue

        break
    except:
        print("Некоторые данные введены неправильно")

for row in range(rows):
    seatsInRow = "=" * seats
    gapInRow = ""
    if(gap > 0):
        gapInRow = " " + "*"*gap + " "
    print(seatsInRow + gapInRow + seatsInRow)