def rotate_number(number):
    result = ""
    for num in range(len(str(number)) - 1, -1, -1):
        result += str(number)[num]
    return int(result)

user_numbers = []
while True:
    try:
        user_number = int(input("Введите число: "))
        user_numbers.append(user_number)
        if(len(user_numbers) == 2):
            break
    except:
        print("Это не число")

print(f"Первое число наоборот: {rotate_number(user_numbers[0])}")
print(f"Второе число наоборот: {rotate_number(user_numbers[1])}")