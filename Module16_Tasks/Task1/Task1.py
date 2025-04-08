class Task1:
    @classmethod
    def main(cls):
        main_list = [1, 5, 3]
        extra_list1 = [1, 5, 1, 5]
        extra_list2 = [1, 3, 1, 5, 3, 3]

        counter = 0
        for number in extra_list1:
            main_list.append(number)
        for number in main_list:
            if(number == 5):
                main_list.remove(number)
                counter +=1
        print(f"Кол-во цифр 5 при первом объединении: {counter}")

        counter = 0
        for number in extra_list2:
            main_list.append(number)
        for number in main_list:
            if(number == 3):
                counter +=1

        print(f"Кол-во цифр 3 при втором объединении: {counter}")
        print(f"Итоговый список: {main_list}")
        return main_list
