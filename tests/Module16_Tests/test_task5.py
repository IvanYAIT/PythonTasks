from Module16_Tasks.Task5.Task5 import Task5

def test_count_songs_duration():
    songs1 = [['World in My Eyes', 4.86],
            ['Sweetest Perfection', 4.43],
            ['Personal Jesus', 4.56]]
    songs2 = []
    assert Task5.count_songs_duration(songs1) == 13.85
    assert Task5.count_songs_duration(songs2) == 0.00