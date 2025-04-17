from Module20_Tasks.Task3.Task3 import Task3

def test_connect_data():
    data1 = { ("Ivan", "Volkin"): (10, 5, 13), ("Bob", "Robbin"): (7, 5, 14), ("Rob", "Bobbin"): (12, 8, 2)}
    data2 = { ():() }
    assert Task3.connect_data(data1) == [('Ivan', 'Volkin', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]
    assert Task3.connect_data(data2) == [()]