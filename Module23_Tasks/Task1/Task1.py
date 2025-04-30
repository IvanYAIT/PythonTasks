import os

class Task1:
    PATH_TO_PEOPLE_FILE = os.path.abspath(__file__).replace('Task1.py', 'people.txt')
    PATH_TO_ERROR_FILE = os.path.abspath(__file__).replace('Task1.py', 'error.log')

    def get_people_from_file(self):
        names = []
        with open(self.PATH_TO_PEOPLE_FILE, 'r', encoding='utf-8') as file:
            names = file.readlines()
        result = []
        for name in names:
            if(name != names[len(names)-1]):
                result.append(name[:-1])
            else:
                result.append(name)
        return result
        
    def count_names_len(self, people):
        result = 0
        with open(self.PATH_TO_ERROR_FILE, '+w', encoding='utf-8') as file:
            for name_index in range(len(people)):
                name_lenght = len(people[name_index])
                if name_lenght >= 3:
                    result += name_lenght 
                else: 
                    error_log = f"Ошибка: менее 3х символов в строке {name_index+1}"
                    file.write(error_log)
                    print(error_log)
        return result
    
    def main(self):
        people = self.get_people_from_file()
        print(people)
        names_len = self.count_names_len(people)
        print(f"Общее количество символов: {names_len}")