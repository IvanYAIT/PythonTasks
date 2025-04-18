from Module20_Tasks.Task5.Task5 import Task5

def test_tpl_sort():
    tpl1 = (6, 3, -1, 8, 4, 10, -5)
    tpl2 = (6.1, 3, -1, 8, 4, 10, -5)
    assert Task5.tpl_sort(tpl1) == (-5, -1, 3, 4, 6, 8, 10)
    assert Task5.tpl_sort(tpl2) == tpl2