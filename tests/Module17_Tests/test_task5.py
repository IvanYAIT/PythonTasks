from Module17_Tasks.Task5.Task5 import Task5

def test_find_reverse_string_btween_h():
    string1 = "hqwehrty"
    string2 = "hh"
    string3 = "hhqwerh"
    assert Task5.find_reverse_string_btween_h(string1) == "ewq"
    assert Task5.find_reverse_string_btween_h(string2) == ""
    assert Task5.find_reverse_string_btween_h(string3) == "rewq"