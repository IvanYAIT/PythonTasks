import random as rnd

def rock_paper_scissors(user_choice):
    list_of_choice = ["камень", "ножницы", "бумага"]
    choice = rnd.randint(0, len(list_of_choice))

    if (user_choice.lower() == list_of_choice[choice]):
        print("Ничья")
    elif (user_choice.lower() == "ножницы" and list_of_choice[choice] == "бумага"
          or user_choice.lower() == "камень" and list_of_choice[choice] == "ножницы"
          or user_choice.lower() == "бумага" and list_of_choice[choice] == "камень"):
        print("Ты выиграл!!!")
    else:
        print("Ты проиграл(")

def guess_number(number, hidden_number):
    if(number == hidden_number):
        return True
    elif(number > hidden_number):
        print(f"Загадонное число меньше {number}")
    elif(number < hidden_number):
        print(f"Загадонное число больше {number}")
    return False

while True:
    print("Выбери игру: \n", 
          "1 - Камень, ножницы, бумага \n", 
          "2 - Угадай число")

    while True:
        try:
            user_input = input()
            if(user_input.lower() == "exit" or user_input.lower() == "выход"):
                break

            command = int(user_input)
            if(command >= 1 and command <= 2):
                break

            print("Введен неправильная команда")
        except:
            print("Это не число")
    
    if(user_input.lower() == "exit" or user_input.lower() == "выход"):
        break

    if(command == 1):
        user_choice = ""
        while True:
            user_choice = input("Выберите камень, ножницы или бумагу: ")
            print(user_choice.lower())
            if(user_choice.lower() == "камень" or user_choice.lower() == "ножницы" or user_choice.lower() == "бумага"):
                break

            print("Неправильная команда")
        rock_paper_scissors(user_choice)
    elif (command == 2):
        hidden_number = rnd.randint(1, 1001)
        while True:
            while True:
                try:
                    user_number = int(input("Введите число: "))

                    if(user_number > 0):
                        break

                    print("Загадонное число больше 0")
                except:
                    print("Это не число")

            if(guess_number(user_number, hidden_number)):
                print(f"Ты угадал это число {hidden_number}")
                break
