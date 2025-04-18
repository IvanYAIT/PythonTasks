from services.user_input import call_until_valid_input

class Task7:
    @call_until_valid_input
    def get_user_list():
        user_input = input("Строка: ")
        return list(user_input)
    
    @call_until_valid_input
    def get_user_tuple(list_len):
        user_tuple = tuple(input("Кортеж чисел(через пробел): ").split(" "))
        if(list_len != len(user_tuple)):
            raise ValueError("Размер кортежа дожен быть равен длине строки")
        return user_tuple

    def archive_gen(list, tpl):
        for item_index in range(len(list)):
            yield (list[item_index], tpl[item_index])

    @classmethod
    def main(cls):
        list = cls.get_user_list()
        tpl = cls.get_user_tuple(len(list))
        zip = cls.archive_gen(list, tpl)
        print(zip)
        for item in zip:
            print(item)