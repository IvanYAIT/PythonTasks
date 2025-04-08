from Module16_Tasks.Task4.Task4 import Task4

def test_try_add_guest():
    guests1 = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
    guests2 = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя', 'Саша']
    guest_name = 'Ваня'
    assert Task4.try_add_guest(guests1, guest_name) == ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя', 'Ваня']
    assert Task4.try_add_guest(guests2, guest_name) == guests2

def test_try_remove_guest():
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя', 'Саша']
    guest_name1 = 'Ваня'
    guest_name2 = 'Кирилл'
    assert Task4.try_remove_guest(guests, guest_name1) == ['Петя', 'Саша', 'Лиза', 'Катя', 'Саша']
    assert Task4.try_remove_guest(guests, guest_name2) == guests