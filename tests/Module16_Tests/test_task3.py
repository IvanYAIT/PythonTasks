from Module16_Tasks.Task3.Task3 import Task3

def test_get_count_and_cost():
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], 
            ['педаль', 100], ['седло', 1500], ['рама', 12000], 
            ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    product1 = "седло"
    product2 = "весло"
    assert Task3.get_count_and_cost(shop, product1) == [3, 4500]
    assert Task3.get_count_and_cost(shop, product2) == [0, 0]
