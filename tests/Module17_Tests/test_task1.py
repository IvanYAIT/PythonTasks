from Module17_Tasks.Task1.Task1 import Task1

def test_find_all_vowels():
    text1 = "Нужно отнести кольцо в Мордор!"
    text2 = "прктрвнцфсчхнтрлдв"
    assert  Task1.find_all_vowels(text1) == ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
    assert  Task1.find_all_vowels(text2) == []