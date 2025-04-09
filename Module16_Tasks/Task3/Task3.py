from services.user_input import call_until_valid_input

class Task3:
    @call_until_valid_input
    def get_product():
        return input("Название детали: ").lower()
    
    def get_count_and_cost(shop, product):
        result = [0, 0]
        for item in shop:
            if(item[0].lower() == product):
                result[0] += 1
                result[1] += item[1]
        
        return result
    
    @classmethod
    def main(cls):
        shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], 
                ['педаль', 100], ['седло', 1500], ['рама', 12000], 
                ['обод', 2000], ['шатун', 200], ['седло', 2700]]
        product_name = cls.get_product()
        product_count_and_cost = cls.get_count_and_cost(shop, product_name)
        print(f"Кол-во деталей - {product_count_and_cost[0]}\n", f"Общая стоимость - {product_count_and_cost[1]}")
