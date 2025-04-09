from services.user_input import call_until_valid_input

class Task8:
    @call_until_valid_input
    def get_list_of_numbers():
        user_string_list = input("Изначальный список: ").split(" ")
        user_number_list = []
        for str in user_string_list:
            user_number_list.append(int(str))

        return user_number_list
    
    def ascending_sort(list):
        for index in range(len(list)):
            current_min_number = list[index]
            index_of_min_number = index
            for number_index in range(index+1, len(list)):
                if(list[number_index] < current_min_number):
                    current_min_number = list[number_index]
                    index_of_min_number = number_index
            if(index != index_of_min_number):
                number_to_swap = list[index]
                list[index] = list[index_of_min_number]
                list[index_of_min_number] =  number_to_swap
        return list
    
    @classmethod
    def main(cls):
        list_of_numbers = cls.get_list_of_numbers()
        sorted_list = cls.ascending_sort(list_of_numbers)
        print(f"Отсортированный список: {sorted_list}")
