from Module17_Tasks.Task2.Task2 import Task2

def test_generate_list():
    lenght1 = 10
    lenght2 = 1
    assert Task2.generate_list(lenght1) == [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]
    assert Task2.generate_list(lenght2) == [1]