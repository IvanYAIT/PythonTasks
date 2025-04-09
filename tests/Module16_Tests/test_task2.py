from Module16_Tasks.Task2.Task2 import Task2

def test_merge_and_sort_list():
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 5, 6, 8, 10]
    assert Task2.merge_and_sort_list(list1, list2) == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}