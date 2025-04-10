from services.user_input import call_until_valid_input

class Task2:
    @call_until_valid_input
    def get_user_string():
        return input("Введите строку: ")

    def compress_string(string):
        result = ""
        counter = 0
        letter_to_count = string[0]
        for char in string:
            if(char == letter_to_count):
                counter += 1
            else:
                result += f"{letter_to_count}{counter}"
                counter = 1
                letter_to_count = char
        else:
            result += f"{letter_to_count}{counter}"
        return result

    @classmethod
    def main(cls):
        user_string = cls.get_user_string()
        compressed_string = cls.compress_string(user_string)
        print(f"Закодированная строка: {compressed_string}")