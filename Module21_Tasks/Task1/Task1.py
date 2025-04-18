from services.user_input import call_until_valid_input

class Task1:
    @call_until_valid_input
    def get_user_number():
        number = int(input("Введите num: "))
        if(number <= 0):
            raise ValueError("Число должно быть больше 0")
        return number

    @classmethod
    def main(cls):
        num = cls.get_user_number()
        array = list(range(1, num+1))
        list(map(print, array))
        