class Task7:
    def get_same_numbers_in_array(array1, array2, array3):
        result = []
        for num in array1:
            if (num in array2 and num in array3):
                result.append(num)
        return result
    
    def get_same_numbers_in_array_using_set(array1, array2, array3):
        result = []
        set1 = set(array1)
        set2 = set(array2)
        set3 = set(array3)
        result = set1.intersection(set2, set3)
        return list(result)
    
    def get_different_numbers_in_arrays(array1, array2, array3):
        result = []
        for num in array1:
            if(num not in array2 and num not in array3):
                result.append(num)
        return result

    def get_different_numbers_in_arrays_using_set(array1, array2, array3):
        set1 = set(array1)
        set2 = set(array2)
        set3 = set(array3)
        result = set1.difference(set2, set3)
        return list(result)

    @classmethod
    def main(cls):
        array1 = [1, 5 , 10, 20, 40, 80, 100]
        array2 = [6, 7, 20, 80, 100]
        array3 = [3, 4, 15, 20, 30, 70, 80, 120]
        same_num = cls.get_same_numbers_in_array(array1, array2, array3)
        same_num_set = cls.get_same_numbers_in_array_using_set(array1, array2, array3)
        different_num = cls.get_different_numbers_in_arrays(array1, array2, array3)
        different_num_set = cls.get_different_numbers_in_arrays_using_set(array1, array2, array3)
        print("Задача 1:")
        print(f"- Решение без множеств: {same_num}", f"\n- Решение c множеств: {same_num_set}")
        print("\nЗадача 2:")
        print(f"- Решение без множеств: {different_num}", f"\n- Решение c множеств: {different_num_set}")
        