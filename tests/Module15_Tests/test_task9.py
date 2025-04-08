from Module15_Tasks.Task9.Task9 import Task9

def test_get_even_numbers_from_list_in_revers_order():
    list1 = [7, 14, 3, 18, 21, 10, 9, 6]
    list2 = [4, 5, 6, 7, 8, 9, 10, 11, 12]
    list3 = [1, 3, 5, 7]
    list4 = [4]
    assert Task9.get_even_numbers_from_list_in_revers_order(list1) == [6, 10, 18, 14]
    assert Task9.get_even_numbers_from_list_in_revers_order(list2) == [12, 10, 8, 6, 4]
    assert Task9.get_even_numbers_from_list_in_revers_order(list3) == []
    assert Task9.get_even_numbers_from_list_in_revers_order(list4) == [4]