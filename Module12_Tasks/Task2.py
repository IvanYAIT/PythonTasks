def test():
    while True:
        try:
            userNumber = int(input("Введите число: "))
            break
        except:
            print("Это не число")
    
    if(userNumber >= 0):
        positive()
    else:
        negative()

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

test()