from services.user_input import call_until_valid_input

class Task5:
    @call_until_valid_input
    def get_user_string():
        user_string = input("Введите строку: ")
        counter = 0
        for char in user_string:
            if(char=="h"):
                counter += 1

        if(counter <= 1):
            raise ValueError
        
        return user_string
    
    def find_reverse_string_btween_h(string):
        end_index = string.rindex("h")
        start_index = string.rindex("h", 0, end_index)

        return string[end_index-1:start_index:-1]
    
    @classmethod
    def main(cls):
        string = cls.get_user_string()
        string_betwen_h= cls.find_reverse_string_btween_h(string)
        print(f"Развёрнутая последовательность между первым и последним h: {string_betwen_h}")