from Module19_Tasks.Task7.Task7 import Task7

def test_get_same_numbers_in_array():
    array1 = [1, 5 , 10, 20, 40, 80, 100]
    array2 = [6, 7, 20, 80, 100]
    array3 = [3, 4, 15, 20, 30, 70, 80, 120]
    assert Task7.get_same_numbers_in_array(array1, array2, array3) == [20, 80]

def test_get_same_numbers_in_array_using_set():
    array1 = [1, 5 , 10, 20, 40, 80, 100]
    array2 = [6, 7, 20, 80, 100]
    array3 = [3, 4, 15, 20, 30, 70, 80, 120]
    assert Task7.get_same_numbers_in_array_using_set(array1, array2, array3) == [80, 20]

def test_get_different_numbers_in_arrays():
    array1 = [1, 5 , 10, 20, 40, 80, 100]
    array2 = [6, 7, 20, 80, 100]
    array3 = [3, 4, 15, 20, 30, 70, 80, 120]
    assert Task7.get_different_numbers_in_arrays(array1, array2, array3) == [1, 5, 10, 40]
    assert Task7.get_different_numbers_in_arrays(array1, array1, array1) == []

def test_get_different_numbers_in_arrays_using_set():
    array1 = [1, 5 , 10, 20, 40, 80, 100]
    array2 = [6, 7, 20, 80, 100]
    array3 = [3, 4, 15, 20, 30, 70, 80, 120]
    assert Task7.get_different_numbers_in_arrays_using_set(array1, array2, array3) == [40, 1, 10, 5]
    assert Task7.get_different_numbers_in_arrays_using_set(array1, array1, array1) == []