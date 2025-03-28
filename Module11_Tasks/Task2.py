import math

while True:
    try:
        numCount = int(input("Введите кол-во чисел: "))

        if(numCount > 0):
            break
        
        print("Чисел должна быть больше 0")
    except:
        print("Это не число")

for _ in range(numCount):
    while True:
        try:
            currentNumber = float(input("Введите число: "))

            if(currentNumber > 0):
                currentNumber = math.ceil(currentNumber)
                print(f"x = {currentNumber} log(x) = {math.log(currentNumber)}")
                break
            elif (currentNumber < 0):
                currentNumber = math.floor(currentNumber)
                print(f"x = {currentNumber} exp(x) = {math.exp(currentNumber)}")
                break
            else:
                print("Число не должно быть равно 0")
        except:
            print("Это не число")