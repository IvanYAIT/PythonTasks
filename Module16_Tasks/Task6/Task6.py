from services.user_input import call_until_valid_input

class Task6:
    @call_until_valid_input
    def get_amount_of_skates():
        skates_amount = int(input("Кол-во коньков: "))
        
        if(skates_amount <= 0):
            raise ValueError

        return skates_amount
    
    @call_until_valid_input
    def get_skates_size(skates_amount):
        result = []
        for index in range(skates_amount):
            skates_size = int(input(f"Размер {index+1} пары: "))
            result.append(skates_size)
        return result
    
    @call_until_valid_input
    def get_amount_of_people():
        people_amount = int(input("Кол-во людей: "))
        
        if(people_amount <= 0):
            raise ValueError

        return people_amount
    
    @call_until_valid_input
    def get_legs_size(people_amount):
        result = []
        for index in range(people_amount):
            leg_size = int(input(f"Размер ноги {index+1} человека: "))
            result.append(leg_size)
        return result
    
    def count_suitable_skates(leg_sizes, skates_sizes):
        result = 0
        leg_sizes = sorted(leg_sizes, reverse=True)
        skates_sizes = sorted(skates_sizes, reverse=True)
        for leg_size in leg_sizes:
            for skates_size in skates_sizes:
                if(skates_size >= leg_size):
                    skates_sizes.remove(skates_size)
                    result += 1
                    break
        return result
    
    @classmethod
    def main(cls):
        skates_amount = cls.get_amount_of_skates()
        skates_sizes = cls.get_skates_size(skates_amount)
        print()
        people_amount = cls.get_amount_of_people()
        leg_sizes = cls.get_legs_size(people_amount)

        people_with_skates = cls.count_suitable_skates(leg_sizes, skates_sizes)
        print(f"Наибольшее кол-во людей, которые могут взять ролики: {people_with_skates}")