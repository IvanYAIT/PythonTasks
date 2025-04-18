import random as rnd

class Task4:
    def generate_array():
        result = []
        for _ in range(10):
            result.append(rnd.randint(0, 10))
        return result
    
    def create_array_of_tuples(array):
        result = []
        for index in range(0, len(array), 2):
            result.append((array[index], array[index+1]))
        return result
    
    def create_array_of_tuples_comprehension(array):
        return [tuple(array[num_index] for num_index in range(index, index + 2)) for index in range(0, len(array), 2)]
    
    @classmethod
    def main(cls):
        generated_array = cls.generate_array()
        array_of_tuples1 = cls.create_array_of_tuples(generated_array)
        array_of_tuples2 = cls.create_array_of_tuples_comprehension(generated_array)
        print(f"Оригинальный список: {generated_array}")
        print(f"Новый список: {array_of_tuples2}")