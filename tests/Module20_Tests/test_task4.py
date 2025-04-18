from Module20_Tasks.Task4.Task4 import Task4

def test_create_array_of_tuples():
    array1 = [1, 2, 3, 4]
    array2 = [1, 2]
    array3 = []
    assert Task4.create_array_of_tuples(array1) == [(1, 2), (3, 4)]
    assert Task4.create_array_of_tuples(array2) == [(1, 2)]
    assert Task4.create_array_of_tuples(array3) == []

def test_create_array_of_tuples_comprehension():
    array1 = [1, 2, 3, 4]
    array2 = [1, 2]
    array3 = []
    assert Task4.create_array_of_tuples_comprehension(array1) == [(1, 2), (3, 4)]
    assert Task4.create_array_of_tuples_comprehension(array2) == [(1, 2)]
    assert Task4.create_array_of_tuples_comprehension(array3) == []    