import os

class Task1:
    PATH_TO_NUMBERS_FILE = os.path.abspath(__file__).replace("Task1.py", "numbers.txt")
    PATH_TO_ANSWER_FILE = os.path.abspath(__file__).replace("Task1.py", "answer.txt")

    def get_numbers_from_file(self):
        result = []
        with open(self.PATH_TO_NUMBERS_FILE, 'r') as file:
            for line in file:
                result.extend([int(char) for char in line.split() if char.isdigit()])  
        return result
    
    def sum_of_numbers(self, numbers):
        return sum(numbers)
    
    def write_number_to_file(self, number):
        with open(self.PATH_TO_ANSWER_FILE, '+w') as file:
            file.write(str(number))


    def main(self):
        numbers = self.get_numbers_from_file()
        sum_of_numbers = self.sum_of_numbers(numbers)
        self.write_number_to_file(sum_of_numbers)
        print(sum_of_numbers)