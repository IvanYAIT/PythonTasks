from Module17_Tasks.Task4.Task4 import Task4

def test_copy_string():
    string = 'abcdefg'
    new_string = Task4.copy_string(string)
    assert id(new_string) == id(string)

def test_reverse_string():
    string = 'abcdefg'
    assert Task4.reverse_string(string) == 'gfedcba'