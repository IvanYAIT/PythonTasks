def rotate_number(number):
    result = ""
    for num in range(len(str(number)) - 1, -1, -1):
        result += str(number)[num]
    return int(result)

userNumbers = []
while True:
    try:
        userNumber = int(input("Введите число: "))
        userNumbers.append(userNumber)
        if(len(userNumbers) == 2):
            break
    except:
        print("Это не число")

print(f"Первое число наоборот: {rotate_number(userNumbers[0])}")
print(f"Второе число наоборот: {rotate_number(userNumbers[1])}")