from Module15_Tasks.Task3.Task3 import Task3

def test_remove_newest_gpu():
    input1 = [2070, 3090, 2070, 3070, 3090]
    input2 = [3090, 3090, 3090, 3070, 3090]
    input3 = [2070, 2070]
    assert Task3.remove_newest_gpu(input1) == [2070, 2070, 3070]
    assert Task3.remove_newest_gpu(input2) == [3070]
    assert Task3.remove_newest_gpu(input3) == []