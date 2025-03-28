def maximum_of_two(num1, num2):
    if(num1 > num2):
        return num1
    return num2

def maximum_of_three(num1, num2, num3):
    return maximum_of_two(num1, maximum_of_two(num2, num3))

userNumbers = []
while True:
    try:
        userNumber = int(input("Введите число: "))
        userNumbers.append(userNumber)
        if(len(userNumbers) == 3):
            break
    except:
        print("Это не число")

print(f"Самое большое число: {maximum_of_three(userNumbers[0], userNumbers[1], userNumbers[2])}")