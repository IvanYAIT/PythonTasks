from Module28_Tasks.Task3.task3 import Date

def test_is_valid_date():
    assert Date.is_valid('10-10-1000') is True
    assert Date.is_valid('50-50-5000') is False
    assert Date.is_valid('10 10 1000') is False
    assert Date.is_valid('0-0-0') is False

def test_date_from_string():
    assert str(Date.from_string('10-10-1000')) == 'День: 10 Месяц: 10 Год: 1000'
    assert str(Date.from_string('50-50-5000')) == 'None'
    assert str(Date.from_string('10 10 1000')) == 'None'
    assert str(Date.from_string('0-0-0')) == 'None'
