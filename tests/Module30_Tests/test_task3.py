from Module30_Tasks.Task3.task3 import Task3

def test_can_be_poly():
    task3 = Task3()
    assert task3.can_be_poly('ababc') is True
    assert task3.can_be_poly('abbbac') is False
    assert task3.can_be_poly('a') is False
    assert task3.can_be_poly('') is False
    assert task3.can_be_poly('aa') is True
    assert task3.can_be_poly('ab') is False