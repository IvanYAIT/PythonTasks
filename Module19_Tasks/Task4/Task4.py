from services.user_input import call_until_valid_input

class Task4:
    @call_until_valid_input
    def get_user_text():
        return input("Введите текст: ")
    
    def convert_text_into_dict(text):
        result = dict()
        for char in text:
            try:
                result[char] += 1
            except:
                result[char] = 1
        return result
    
    def inverse_dict(dict_of_chars):
        result = dict()
        for key in dict_of_chars:
            try:
                result[dict_of_chars[key]].append(key)
            except:
                result[dict_of_chars[key]] = [key]
        return result

    @classmethod
    def main(cls):
        user_text = cls.get_user_text()
        dict_of_chars = cls.convert_text_into_dict(user_text)
        for key in dict_of_chars.keys():
            print(f"{key} : {dict_of_chars[key]}")
        print("\nИнвертированный словарь частот:")
        inversed_dict = cls.inverse_dict(dict_of_chars)
        for key in inversed_dict.keys():
            print(f"{key} : {inversed_dict[key]}")