import random as rnd

def rock_paper_scissors(userChoice):
    listOfChoice = ["камень", "ножницы", "бумага"]
    choice = rnd.randint(0, len(listOfChoice))

    if (userChoice.lower() == listOfChoice[choice]):
        print("Ничья")
    elif (userChoice.lower() == "ножницы" and listOfChoice[choice] == "бумага"
          or userChoice.lower() == "камень" and listOfChoice[choice] == "ножницы"
          or userChoice.lower() == "бумага" and listOfChoice[choice] == "камень"):
        print("Ты выиграл!!!")
    else:
        print("Ты проиграл(")

def guess_number(number, hiddenNumber):
    if(number == hiddenNumber):
        return True
    elif(number > hiddenNumber):
        print(f"Загадонное число меньше {number}")
    elif(number < hiddenNumber):
        print(f"Загадонное число больше {number}")
    return False

while True:
    print("Выбери игру: \n", 
          "1 - Камень, ножницы, бумага \n", 
          "2 - Угадай число")

    while True:
        try:
            userInput = input()
            if(userInput.lower() == "exit" or userInput.lower() == "выход"):
                break

            command = int(userInput)
            if(command >= 1 and command <= 2):
                break

            print("Введен неправильная команда")
        except:
            print("Это не число")
    
    if(userInput.lower() == "exit" or userInput.lower() == "выход"):
        break

    if(command == 1):
        userChoice = ""
        while True:
            userChoice = input("Выберите камень, ножницы или бумагу: ")
            print(userChoice.lower())
            if(userChoice.lower() == "камень" or userChoice.lower() == "ножницы" or userChoice.lower() == "бумага"):
                break

            print("Неправильная команда")
        rock_paper_scissors(userChoice)
    elif (command == 2):
        hiddenNumber = rnd.randint(1, 1001)
        while True:
            while True:
                try:
                    userNumber = int(input("Введите число: "))

                    if(userNumber > 0):
                        break

                    print("Загадонное число больше 0")
                except:
                    print("Это не число")

            if(guess_number(userNumber, hiddenNumber)):
                print(f"Ты угадал это число {hiddenNumber}")
                break
