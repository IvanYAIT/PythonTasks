from services.user_input import call_until_valid_input

class Task6:
    @call_until_valid_input
    def get_orders_amount():
        amount = int(input("Введите кол-во заказов: "))

        if(amount <= 0):
            raise ValueError("Количество заказов должно быть больше нуля")
        
        return amount
    
    @call_until_valid_input
    def get_people_orders(orders_amount):
        result = dict()
        for index in range(orders_amount):
            person_order = [order_part.lower() for order_part in input(f"{index+1} заказ: ").split(" ")]
            if(result.get(person_order[0]) is None):
                result[person_order[0]] = {person_order[1] : int(person_order[2])}
            else:
                if(result[person_order[0]].get(person_order[1]) is None):
                    result[person_order[0]][person_order[1]] = int(person_order[2])
                else:
                    result[person_order[0]][person_order[1]] += int(person_order[2])
        return result
    
    def print_orders(people_orders):
        for person_order in people_orders.keys():
            print(f"{person_order}: ")
            for order in people_orders[person_order].keys():
                print(f"    {order}: {people_orders[person_order][order]}")

    @classmethod
    def main(cls):
        orders_amount = cls.get_orders_amount()
        orders = cls.get_people_orders(orders_amount)
        cls.print_orders(orders)
                    