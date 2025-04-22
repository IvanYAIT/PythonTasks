from Module21_Tasks.Task5.Task5 import Task5

def test_unpack_array():
    array = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], 
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
    task = Task5()
    assert task.unpack_array(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]