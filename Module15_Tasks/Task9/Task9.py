from services.user_input import call_until_valid_input

class Task9:
    @call_until_valid_input
    def get_list_of_numbers():
        user_string_list = input("Изначальный список: ").split(" ")
        user_number_list = []
        for str in user_string_list:
            user_number_list.append(int(str))

        return user_number_list
    
    def get_even_numbers_from_list_in_revers_order(list):
        number_index = 0
        for _ in range(len(list)):
            if(list[number_index] % 2 != 0):
                list.remove(list[number_index])
                number_index -= 1
            number_index += 1

        middle_index = len(list)//2 if len(list) % 2 != 0 else (len(list)//2)-1

        for index in range(len(list)-1, middle_index, -1):
            current_number = list[index]
            list[index] = list[len(list) - 1 - index]
            list[len(list) -1 - index] = current_number            

        return list
    
    @classmethod
    def main(cls):
        user_list = cls.get_list_of_numbers()
        list_of_even_numbers = cls.get_even_numbers_from_list_in_revers_order(user_list)
        print(f"Четные числа в обратном порядке: {list_of_even_numbers}")