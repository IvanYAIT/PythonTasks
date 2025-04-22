class Task3:
    def print_store_items(goods, store):
        for item in goods.keys():
            cost = 0
            quantity = 0
            for item_info in store[goods[item]]:
                cost += item_info["quantity"] * item_info["price"]
                quantity += item_info["quantity"]
            print(f"{item} - {quantity} шт, стоимость {cost} руб")

    @classmethod
    def main(cls):
        goods = {
            'Лампа': '12345',
            'Стол': '23456',
            'Диван': '34567',
            'Стул': '45678',
        }

        store = {
            '12345': [
                {'quantity': 27, 'price': 42},
            ],
            '23456': [
                {'quantity': 22, 'price': 510},
                {'quantity': 32, 'price': 520},
            ],
            '34567': [
                {'quantity': 2, 'price': 1200},
                {'quantity': 1, 'price': 1150},
            ],
            '45678': [
                {'quantity': 50, 'price': 100},
                {'quantity': 12, 'price': 95},
                {'quantity': 43, 'price': 97},
            ],
        }
        cls.print_store_items(goods, store)