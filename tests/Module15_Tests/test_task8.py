from Module15_Tasks.Task8.Task8 import Task8

def test_ascending_sort():
    list1 = [1, 4, -3, 0, 10]
    list2 = [0, 0, 0]
    list3 = [1]
    list4 = [1, 2, 3]
    assert Task8.ascending_sort(list1) == [-3, 0, 1, 4, 10]
    assert Task8.ascending_sort(list2) == [0, 0, 0]
    assert Task8.ascending_sort(list3) == [1]
    assert Task8.ascending_sort(list4) == [1, 2, 3]