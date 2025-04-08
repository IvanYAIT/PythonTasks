from Module15_Tasks.Task1.Task1 import Task1

def test_find_odd_numbers_to_number():
    assert Task1.find_odd_numbers_to_number(1) == [1]
    assert Task1.find_odd_numbers_to_number(5) == [1, 3, 5]
    assert Task1.find_odd_numbers_to_number(6) == [1, 3, 5]