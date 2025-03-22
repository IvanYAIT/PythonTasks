import random

hiddenNumber = random.randint(1, 100)
attempts = 0
userNumber = hiddenNumber -1

while (userNumber != hiddenNumber):
    while True:
        try:
            userNumber = int(input("Введите число: "))
        except:
            print("Это не число")
        else:
            break
    

    if(userNumber < hiddenNumber):
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif(userNumber > hiddenNumber):
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    attempts += 1

print(f"Вы угадали! Число попыток: {attempts}")