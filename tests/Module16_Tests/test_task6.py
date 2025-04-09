from Module16_Tasks.Task6.Task6 import Task6

def test_count_suitable_skates():
    skates_sizes1 = [41, 39, 40, 42]
    skates_sizes2 = [38, 38, 38]
    leg_sizes1 = [42, 41, 42]
    leg_sizes2 = [38, 38, 38]
    leg_sizes3 = [41]
    assert Task6.count_suitable_skates(leg_sizes1, skates_sizes1) == 2
    assert Task6.count_suitable_skates(leg_sizes2, skates_sizes2) == 3
    assert Task6.count_suitable_skates(leg_sizes3, skates_sizes2) == 0