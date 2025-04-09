from Module14_Tasks.Task3.Task3 import Task3

def test_find_min_divider():
    assert Task3.find_min_divider(17) == 17
    assert Task3.find_min_divider(6) == 2
    assert Task3.find_min_divider(9) == 3