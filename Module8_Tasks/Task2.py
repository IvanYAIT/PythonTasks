while True:
    try:
        amountOfPeople = int(input("Введите количество должников: "))
        break
    except:
        print("Это не число")

sumOfDepts = 0
for personNumbr in range(0, amountOfPeople , 5):
    print(f"Должник с номером {personNumbr}")
    while True:
        try:
            sumOfDepts += int(input(f"Сколько должны? "))
            break
        except:
            print("Это не число")

print(f"Общая сумма долга: {sumOfDepts}")
