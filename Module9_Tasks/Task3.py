x = 8
y = 10
while True:
    print(f"[Программа]: Марсоход находится на позиции ({x}, {y}), введите команду: ")
    userInput = input("[Оператор]: ").lower()

    if(userInput == "exit"):
        break

    if(userInput != "w" and userInput != "a" and userInput != "s" and userInput != "d"):
        print("Введина неправильная комнда")
        continue

    if(userInput == "w"):
        x += 1
    elif(userInput == "s"):
        x-= 1
    elif(userInput == "d"):
        y += 1
    elif(userInput == "a"):
        y -= 1

    if(x > 15):
        x = 15
    elif( x < 0):
        x = 0

    if(y > 20):
        y = 20
    elif(y < 0):
        y = 0