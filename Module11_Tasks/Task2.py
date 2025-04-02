import math

while True:
    try:
        num_count = int(input("Введите кол-во чисел: "))

        if(num_count > 0):
            break
        
        print("Чисел должна быть больше 0")
    except:
        print("Это не число")

for _ in range(num_count):
    while True:
        try:
            current_number = float(input("Введите число: "))

            if(current_number > 0):
                current_number = math.ceil(current_number)
                print(f"x = {current_number} log(x) = {math.log(current_number)}")
                break
            elif (current_number < 0):
                current_number = math.floor(current_number)
                print(f"x = {current_number} exp(x) = {math.exp(current_number)}")
                break
            else:
                print("Число не должно быть равно 0")
        except:
            print("Это не число")