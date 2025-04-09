from Module15_Tasks.Task6.Task6 import Task6

def test_apply_shift_to_sequence():
    sequence = [1, 2, 3, 4, 5]
    shift = 1
    expected_result = [5, 1, 2, 3, 4]
    assert Task6.apply_shift_to_sequence(sequence, shift) == expected_result