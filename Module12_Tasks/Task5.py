import random as rnd
from services.user_input import call_until_valid_input

@call_until_valid_input
def get_command():
    user_input = input()
    if(user_input.lower() == "exit" or user_input.lower() == "выход"):
        return user_input

    command = int(user_input)
    if(command < 1 or command > 2):
        raise ValueError

    return command

@call_until_valid_input
def get_user_choice():
    user_choice = input("Выберите камень, ножницы или бумагу: ")

    if(user_choice.lower() != "камень" and user_choice.lower() != "ножницы" and user_choice.lower() != "бумага"):
        raise
    
    return user_choice

@call_until_valid_input
def get_user_number():
    user_number = int(input("Введите число: "))

    if(user_number < 0):
        raise ValueError
    
    return user_number

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

    command = get_command()
    
    if(str(command).lower() == "exit" or str(command).lower() == "выход"):
        break

    if(command == 1):
        user_choice = get_user_choice()

        rock_paper_scissors(user_choice)
    elif (command == 2):
        hidden_number = rnd.randint(1, 1001)
        
        while True:
            user_number = get_user_number()

            if(guess_number(user_number, hidden_number)):
                print(f"Ты угадал это число {hidden_number}")
                break
