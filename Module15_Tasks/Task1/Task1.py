from services.user_input import call_until_valid_input

class Task1:
    @call_until_valid_input
    def get_user_number():
        user_number = int(input("Введите число: "))

        if(user_number <= 0):
            raise ValueError
        
        return user_number
    
    def find_odd_numbers_to_number(number):
        result = []
        for num in range(1, number+1):
            if(num % 2 != 0):
                result.append(num)
        return result
    
    @classmethod
    def main(cls):
        number = cls.get_user_number()
        oddNumbers = cls.find_odd_numbers_to_number(number)
        print(f"Список из нечётных чисел от одного до N: {oddNumbers}")