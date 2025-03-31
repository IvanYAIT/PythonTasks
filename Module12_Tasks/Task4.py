def count_letters(text):
    while True:
        try:
            number = input("Какую цифру ищем? ")
            int(number)
            if(len(number) != 1):
                raise 

            if(int(number) >= 0):
                break

            print("Цифра должно быть больше 0")
        except:
            print("Это не цифра")
    
    while True:
        try:
            letter = input("Какую букву ищём? ")
            int(letter)
            print("Это не буква")
        except:
            if(len(letter) == 1):
                break

            print("Это не буква")
    
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
