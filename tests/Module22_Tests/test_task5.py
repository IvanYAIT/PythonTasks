from Module22_Tasks.Task5.Task5 import Task5

def test_count_letters():
    text1 = "Mama myla ramu."
    text2 = "aaaaaaaaaa"
    text3 = ""
    task = Task5()
    assert task.count_letters(text1) == {'a': 4, 'm': 4, 'y': 1, 'l': 1, 'r': 1, 'u': 1}
    assert task.count_letters(text2) == {'a': 10}
    assert task.count_letters(text3) == {}

def test_get_analysis_from_text():
    letters1 = {'a': 4, 'm': 4, 'y': 1, 'l': 1, 'r': 1, 'u': 1}
    letters2 = {'a': 10}
    letters3 = {}
    task = Task5()
    assert task.get_analysis_from_text(letters1) == {'m': 0.333, 'a': 0.333, 'y': 0.083, 'l': 0.083, 'r': 0.083, 'u': 0.083}
    assert task.get_analysis_from_text(letters2) == {'a': 1.000}
    assert task.get_analysis_from_text(letters3) == {}