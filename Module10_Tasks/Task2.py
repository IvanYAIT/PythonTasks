while True:
    try:
        userInput = int(input("Введите число: "))
        if(userInput > 0):
            break

        print("Число должно быть больше нуля")
    except:
        print("Это не число")

for number in range(1, userInput+1):
    print(f"{number} " * number)