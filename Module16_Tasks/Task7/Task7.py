from services.user_input import call_until_valid_input

class Task7:
    @call_until_valid_input
    def get_list_of_people():
        people_amount = int(input("Кол-во человек: "))
        
        if(people_amount <= 0):
            raise ValueError

        return list(range(1,people_amount+1))
    
    @call_until_valid_input
    def get_user_number():
        user_number = int(input("Какое число в считалке? "))
        
        if(user_number <= 0):
            raise ValueError

        print(f"Значит, выбывает каждый {user_number} человек")
        return user_number
    
    def play_counting_rhymes(people, number):
        index = 0
        while len(people) > 1:
            print()
            print(f"Текущий круг людей: {people}")
            print(f"Начало счёта с номера {people[index]}")

            counter = 0
            while True:
                for _ in range(index, len(people)):
                    counter += 1
                    if(counter == number):
                        index = index
                        break
                    index += 1
                if(counter == number):
                        break
                index = 0
            
            print(f"Выбывает человек под номером {people[index]}")
            people.remove(people[index])
            if(index > len(people)-1):
                index = 0
        return people[0]
    
    @classmethod
    def main(cls):
        list_of_people = cls.get_list_of_people()
        number = cls.get_user_number()
        winner = cls.play_counting_rhymes(list_of_people, number)
        print(f"\nОстался человек под номером {winner}")
        