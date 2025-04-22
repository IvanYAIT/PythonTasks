from Module21_Tasks.Task4.Task4 import Task4

def test_advanced_sum():
    array1 = [[1, 2, [3]], [1], 3]
    task = Task4()
    assert task.advanced_sum(array1) == 10
    assert task.advanced_sum(1, 2, 3, 4, 5) == 15