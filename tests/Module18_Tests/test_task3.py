from Module18_Tasks.Task3.Task3 import Task3

def test_apply_shift_to_string():
    string1 = "cdab"
    string2 = "a"
    task = Task3()
    assert task.apply_shift_to_string(string1, 1) == "bcda"
    assert task.apply_shift_to_string(string2, 1) == "a"

def test_try_compare_strings():
    string1 = "abcd"
    string2 = "cdab"
    string3 = "cdba"
    task = Task3()
    assert task.try_compare_strings(string1, string2) == 2
    assert task.try_compare_strings(string1, string3) == -1