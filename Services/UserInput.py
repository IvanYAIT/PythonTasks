def get_user_positive_number(numberType):
    while True:
        try:
            if(numberType.lower() == "int"):
                user_number = int(input("Введите число: "))
            elif(numberType.lower() == "float"):
                user_number = float(input("Введите число: "))

            if(user_number <= 0):
                print("Число должно быть больше 0")
                raise ValueError
    
            break
        except:
            print("Это не число")
    return user_number

def get_user_any_number(numberType):
    while True:
        try:
            if(numberType.lower() == "int"):
                user_number = int(input("Введите число: "))
            elif(numberType.lower() == "float"):
                user_number = float(input("Введите число: "))
            break
        except:
            print("Это не число")
    return user_number