from Module16_Tasks.Task7.Task7 import Task7

def test_play_counting_rhymes():
    list_of_people1 = list(range(1, 6))
    list_of_people2 = list(range(1, 6))
    assert Task7.play_counting_rhymes(list_of_people1, 7) == 4
    assert Task7.play_counting_rhymes(list_of_people2, 2) == 3