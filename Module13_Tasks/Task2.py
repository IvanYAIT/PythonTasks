def maximum_of_two(num1, num2):
    if(num1 > num2):
        return num1
    return num2

def maximum_of_three(num1, num2, num3):
    return maximum_of_two(num1, maximum_of_two(num2, num3))

user_numbers = []
while True:
    try:
        user_number = int(input("Введите число: "))
        user_numbers.append(user_number)
        if(len(user_numbers) == 3):
            break
    except:
        print("Это не число")

print(f"Самое большое число: {maximum_of_three(user_numbers[0], user_numbers[1], user_numbers[2])}")