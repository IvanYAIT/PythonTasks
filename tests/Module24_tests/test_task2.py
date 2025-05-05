from Module24_Tasks.Task2.Task2 import Student

def test_get_average_mark():
    student1 = Student('student1', 1, [1, 1, 1, 1, 1])
    student2 = Student('student2', 1, [])
    student3 = Student('student3', 1, [5])
    assert student1.get_average_mark() == 1
    assert student2.get_average_mark() == 0
    assert student3.get_average_mark() == 5