from services.user_input import call_until_valid_input

class Task3:
    @call_until_valid_input
    def get_user_string():
        return input("Введите строку: ")
        
    def apply_shift_to_string(self, user_string, shift):
        result = []
        for _ in range(len(user_string)):
            result.append(0)
        for index in range(len(user_string)-1, -1, -1):
            newIndex = index + shift
            if(newIndex >= len(user_string)):
                newIndex = newIndex - len(user_string)
            result[newIndex] = user_string[index]
        shifted_string = ""
        for char in result:
            shifted_string += char
        return shifted_string

    def try_compare_strings(self, user_string, string_to_compare):
        shift = 1
        while True:
            if(shift >= len(user_string)):
                return -1
            shifted_string = self.apply_shift_to_string(user_string, shift)
            if(shifted_string == string_to_compare):
                return shift
            else:
                shift += 1
                shifted_string = ""

    def main(self):
        user_string = self.get_user_string()
        string_to_compare = self.get_user_string()
        shift = self.try_compare_strings(user_string, string_to_compare)
        if(shift >= 0):
            print(f"Первая строка получается из второй со сдвигом {shift}")
        else:
            print(f"Первую строку нельзя получить из второй с помощью циклического сдвига")