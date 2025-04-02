def count_numbers(number):
    return len(str(number))

def change_number(number):
    result = ""
    nums_of_number = list(str(number))
    first_num = nums_of_number[0]
    nums_of_number[0] = nums_of_number[count_numbers(number)-1]
    nums_of_number[count_numbers(number)-1] = first_num
    result = ''.join(nums_of_number)
    return int(result)

def main():
    first_number = None
    second_number = None

    while True:
        try:
            if(first_number is None):
                first_number = int(input("Введите первое число: "))

            if(len(str(first_number)) < 3 or first_number < 0):
                print("Первое число должно быть трехзначным или больше")
                first_number = None
                continue

            if(second_number is None):
                second_number = int(input("Введите второе число: "))

            if(len(str(second_number)) < 4 or second_number < 0):
                print("Второе число должно быть четырехзначное или больше")
                second_number = None
                continue

            user_numbers = [first_number, second_number]
            break
        except:
            print("Это не число")
    
    for index in range(len(user_numbers)):
        user_numbers[index] = change_number(user_numbers[index])

    print(f"Сумма чисел равна: {user_numbers[0] + user_numbers[1]}")

main()