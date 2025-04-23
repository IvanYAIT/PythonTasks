import os

class Task2:
    PATH_TO_ZEN_FILE = os.path.abspath(__file__).replace("Task2.py", "zen.txt")

    def get_text_from_file(self):
        result = []
        try:
            with open(self.PATH_TO_ZEN_FILE, 'r') as file:
                for line in file:
                    result.append(line) 
        except:
            print("Такого файла нет")
        return result
    
    def print_text_backwars(self, text):
        for line in text[::-1]:
            print(line)
    
    def main(self):
        text = self.get_text_from_file()
        self.print_text_backwars(text)