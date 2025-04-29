from Module22_Tasks.Task6.Task6 import Task6

def test_count_letters_in_text():
    text1 = 'Text'
    text2 = 'TtTeT'
    text3 = ''
    text4 = 'aaaaa'
    task = Task6()
    assert task.count_letters_in_text(text1, result={}) == {'T': 1, 'e': 1, 'x': 1, 't': 1}
    assert task.count_letters_in_text(text2, result={}) == {'T': 3, 't': 1, 'e': 1}
    assert task.count_letters_in_text(text3, result={}) == {}
    assert task.count_letters_in_text(text4, result={}) == {'a': 5}