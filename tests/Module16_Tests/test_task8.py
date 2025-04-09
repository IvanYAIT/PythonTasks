from Module16_Tasks.Task8.Task8 import Task8

def test_is_numbere_symmetrical():
    number1 = 123321
    number2 = 12321
    number3 = 12345
    task = Task8()
    assert task.is_numbere_symmetrical(number1) == True
    assert task.is_numbere_symmetrical(number2) == True
    assert task.is_numbere_symmetrical(number3) == False

def test_try_find_missing_number():
    left_part1 = [3, 2, 1]
    left_part2 = [5, 6, 7]
    left_part3 = [1, 2,  3]

    right_part1 = [3, 2]
    right_part2 = [5]
    right_part3 = [3, 2, 1]
    
    task = Task8()
    assert task.try_find_missing_number(left_part1, right_part1) == [1]
    assert task.try_find_missing_number(left_part2, right_part2) == [6, 7]
    assert task.try_find_missing_number(left_part3, right_part3) == []

def test_get_missing_numbers():
    sequence1 = [1, 2, 1, 2, 2]
    sequence2 = [1, 2, 3, 4, 5]
    sequence3 = [1, 2, 3, 2]
    sequence4 = [1, 2, 3, 2, 2]
    task = Task8()
    assert task.get_missing_numbers(sequence1) == [1, 2, 1]
    assert task.get_missing_numbers(sequence2) == [4, 3, 2, 1]
    assert task.get_missing_numbers(sequence3) == [1]
    assert task.get_missing_numbers(sequence4) == [3, 2, 1]