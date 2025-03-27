import math

while True:
    userInput = input("Введите число: ")
    try:
        userNumber = int(userInput)
    except:
        print("Это не число")
    else:
        break

for num in range(userNumber+1):
    print(num**3)