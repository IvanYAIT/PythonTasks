from Task1.Task1 import Task1

def print_sequences():
    task1 =Task1()

    sequence1 = task1.get_sequence(1, 2, 3, 4, 5)
    generator1 = task1.generate_sequence(1, 2, 3, 4, 5)
    sequence2 = []
    for num in generator1:
        sequence2.append(num)
    generator2 = task1.generate_sequence_expression(1, 2, 3, 4, 5)
    sequence3 = []
    for num in generator2:
        sequence3.append(num)

    print(f'1: {sequence1}\n', f'2: {sequence2}\n', f'3: {sequence3}')

print_sequences()