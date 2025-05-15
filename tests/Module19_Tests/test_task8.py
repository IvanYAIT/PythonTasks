from Module19_Tasks.Task8.Task8 import Task8

def test_is_string_transformate_in_palindrom():
    string1 = "aab"
    string2 = "aabc"
    string3 = "a"
    string4 = ""
    assert Task8.is_string_transformate_in_palindrom(string1) == True
    assert Task8.is_string_transformate_in_palindrom(string2) == False
    assert Task8.is_string_transformate_in_palindrom(string3) == False
    assert Task8.is_string_transformate_in_palindrom(string4) == False