from Module18_Tasks.Task2.Task2 import Task2

def test_compress_string():
    string1 = "aaAAbbсaaaA"
    string2 = "aAbBcCdD"
    assert Task2.compress_string(string1) == "a2A2b2с1a3A1"
    assert Task2.compress_string(string2) == "a1A1b1B1c1C1d1D1"