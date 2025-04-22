from Module21_Tasks.Task6.Task6 import Task6

def test_fast_sort():
    array1 = [5, 8, 9, 4, 2, 9, 1, 8]
    array2 = [5, 4, 3, 2, 1]
    array3 = [9, 9]
    task = Task6()
    assert task.fast_sort(array1) == [1, 2, 4, 5, 8, 8, 9, 9]
    assert task.fast_sort(array2) == [1, 2, 3, 4, 5]
    assert task.fast_sort(array3) == [9, 9]