from Module22_Tasks.Task4.Task4 import Task4

def test_find_winners():
    array1 = [['Ivanov', 'Serg', '80\n'], ['Segeev', 'Petr', '92\n'], ['Petrov', 'Vasiliy', '98\n'], ['Vasiliev', 'Maxim', '78']]
    array2 = [['Ivanov', 'Serg', '80\n'], ['Segeev', 'Petr', '92\n'], ['Petrov', 'Vasiliy', '98\n'], ['Vasiliev', 'Maxim', '78']]
    array3 = [['Ivanov', 'Serg', '80\n']]
    task = Task4()
    assert task.find_winners(80, array1) == {'V. Petrov': 98, 'P. Segeev': 92}
    assert task.find_winners(60, array2) == {'V. Petrov': 98, 'P. Segeev': 92, 'S. Ivanov': 80, 'M. Vasiliev': 78}
    assert task.find_winners(100, array3) == {}