from Module17_Tasks.Task8.Task8 import Task8

def test_encrypt_text():
    text1 = "а"
    text2 = "это питон"
    assert Task8.encrypt_text(text1, 3) == "г"
    assert Task8.encrypt_text(text2, 3) == "ахс тлхср"