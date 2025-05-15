class Task2:
    def zip_lists(self, letters, numbers):
        return [(letters[index], numbers[index]) for index in range(len(letters))]
    
    def main(self):
        strings: list[str] = ['a', 'b', 'c', 'd', 'e']
        numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
        zip_list = self.zip_lists(strings, numbers)
        print(zip_list)