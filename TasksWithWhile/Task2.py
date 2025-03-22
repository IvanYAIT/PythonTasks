while True:
    userInput = input("Введите число: ")
    try:
        userNumber = int(userInput)
    except:
        print("Это не целое число")
    else:
        if(userNumber >= 0):
            break
        print("Число не положительное")

print(len(userInput))