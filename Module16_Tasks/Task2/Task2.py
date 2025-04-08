from services.user_input import call_until_valid_input

class Task2:
    @call_until_valid_input
    def get_list_of_numbers():
        user_list = input("Введите массив чисел: ").split(" ")
        list_of_numbers = []
        for str in user_list:
            list_of_numbers.append(int(str))
        return list_of_numbers
    
    def merge_and_sort_list(list1, list2):
        for number in list2:
            list1.append(number)
        list1 = sorted(list1)
        return set(list1)
    
    @classmethod
    def main(cls):
        list1 = cls.get_list_of_numbers()
        list2 = cls.get_list_of_numbers()
        sorted_list = cls.merge_and_sort_list(list1, list2)
        print(sorted_list)
    
