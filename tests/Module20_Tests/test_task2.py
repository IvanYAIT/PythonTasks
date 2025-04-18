from Module20_Tasks.Task2.Task2 import Task2

def test_crypto():
    array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array2 = "О Дивный новый мир!"
    array3 = [0, 1]
    task = Task2()
    assert task.crypto(array1) == [2, 3, 5, 7]
    assert task.crypto(array2) == ["Д", "и", "н", "й", "в", "й", "р"]
    assert task.crypto(array3) == []