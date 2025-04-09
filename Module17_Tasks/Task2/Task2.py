from services.user_input import call_until_valid_input

class Task2:
    @call_until_valid_input
    def get_list_array():
        lenght = int(input("Введите длину списка: "))

        if(lenght <= 0):
            raise ValueError
        
        return lenght
    
    def generate_list(list_lenght):
        result = []
        for index in range(list_lenght):
            if(index % 2 == 0):
                result.append(1)
            else:
                result.append(index % 5)
        return result
    
    @classmethod
    def main(cls):
        list_lenght = cls.get_list_array()
        generated_list = cls.generate_list(list_lenght)
        print(f"Результат: {generated_list}")