class Task7:
    def main():
        nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
        list_from_matrix = [x for z in nice_list for y in z for x in y]
        print(list_from_matrix)