table = []

for row in range(6):
    table.append(list(range(row, row + 11, 2)))
    for number in range(len(table[row])): 
        print(table[row][number], end = ' ')
    print()