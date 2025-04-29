import os
from zipfile import ZipFile

class Task6:
    PATH_TO_ARCHIVE = os.path.abspath(__file__).replace("Task6.py", "voina-i-mir.zip")
    EXTRACT_PATH = os.path.abspath(__file__).replace("Task6.py", "")
    PATH_TO_FOLDER = PATH_TO_ARCHIVE.replace('.zip', '')
    ALPHABET = 'qazwsxedcrfvtgbyhnujmikolp'

    def count_letters_in_text(self, text, result):
        for letter in text:
            for char in self.ALPHABET:
                if(letter == char or letter == char.upper()):
                    if result.get(letter):
                        result[letter] += 1
                    else:
                        result[letter] = 1
        return result

    def read_files_from_archive(self):
        result = {}
        with ZipFile(self.PATH_TO_ARCHIVE, "r") as myzip:
            myzip.extractall(path=self.EXTRACT_PATH)
            
        for file_in_archive in os.listdir(self.PATH_TO_FOLDER):
            with open(self.PATH_TO_FOLDER + f"\\{file_in_archive}", 'r') as file:
                self.count_letters_in_text(file.read(), result)
        result = dict(sorted(result.items(), key=lambda item : item[1], reverse=True))
        return result
    
    def print_dict(self, dictionary):
        for key in dictionary.keys():
            print(f"{key} : {dictionary[key]}")
    
    def main(self):
        letters_amount = self.read_files_from_archive()
        self.print_dict(letters_amount)