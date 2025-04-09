from services.user_input import call_until_valid_input

@call_until_valid_input
def get_user_number():
    number = input("Какую цифру ищем? ")
    if(not number.isnumeric()):
        raise ValueError()
            
    if(len(number) != 1):
        raise 

    if(int(number) < 0):
        raise
    
    return number

@call_until_valid_input
def get_user_letter():
    letter = input("Какую букву ищём? ")
    if(letter.isnumeric()):
        raise ValueError()
    
    if(len(letter) != 1):
        raise

    return letter

def count_letters(text):
    number = get_user_number()
    letter = get_user_letter()

    number_count = 0
    letter_count = 0

    for char in text:
        if(char == number):
            number_count += 1
        elif(char == letter):
            letter_count += 1
    
    print(f"Количество цифр {number}: {number_count}\n", f"Количество букв {letter}: {letter_count}")

user_text = input("Введите текст: ")
count_letters(user_text)
