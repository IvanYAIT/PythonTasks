def test():
    while True:
        try:
            user_number = int(input("Введите число: "))
            break
        except:
            print("Это не число")
    
    if(user_number >= 0):
        positive()
    else:
        negative()

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

test()