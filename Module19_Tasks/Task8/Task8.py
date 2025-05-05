from services.user_input import call_until_valid_input

class Task8:
    @call_until_valid_input
    def get_user_string():
        return input("Введите строку: ")

    def is_string_transformate_in_palindrom(string):
        if(len(string) <= 1):
            return False
        chars_amount = dict()
        for char in string:
            try:
                chars_amount[char.lower()] += 1
            except:
                chars_amount[char.lower()] = 1
        counter = 0
        for char_key in chars_amount.keys():
            if(chars_amount[char_key] % 2 != 0):
                counter += 1
            if(counter >=2):
                return False
        return True

    @classmethod
    def main(cls):
        string = cls.get_user_string()
        if(cls.is_string_transformate_in_palindrom(string)):
            print("Можно сделать палиндромом")
        else:
            print("Нельзя сделать палиндромом")