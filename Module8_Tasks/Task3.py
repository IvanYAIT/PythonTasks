while True:
    try:
        reverseTimer = int(input("Введите время для обратного отсчёта (в секундах): "))
        if(reverseTimer > 0):
            print(f"Таймер установлен на {reverseTimer} секунд.")
            break

        print("Таймер нельзя постаить отрицательное время или 0")
    except:
        print("Это не число")

for currentTime in range(reverseTimer, 0, -1):
    print(f"Осталось: {currentTime} секунд")
    while True:
        try:
            userInput = int(input("Введите 1, если еда готова, или 0, чтобы продолжить: "))
            
            if(userInput == 1 or userInput == 0):
                break

            print("Введена неправильная команда")
        except:
            print("Это не число")
    
    if(userInput == 1):
        print(f"Ваша еда готова, можете забрать! Таймер был прерван на {currentTime} секундах.")
        break

    if(currentTime <= 1):
        print("Ваша еда готова. Осторожно, горячo!")
