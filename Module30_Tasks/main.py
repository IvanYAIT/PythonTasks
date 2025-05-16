from Task1.task1 import Task1
from Task2.task2 import Task2
from Task3.task3 import Task3
from Task4.task4 import Task4

def check_task2():
    task2 = Task2()
    task2.main()

def check_polindroms():
    task3 = Task3()
    print(task3.can_be_poly('ababc'))
    print(task3.can_be_poly('abbbc'))

def decrypt_text():
    text = 'Today is a beautiful day! The sun is shining and the birds are singing.'
    task4 = Task4()
    print(task4.decrypt(text))

#Task1.main()
#check_task2()
#check_polindroms()
decrypt_text()
