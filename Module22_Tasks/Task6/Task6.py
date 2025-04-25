import os
from zipfile import ZipFile

class Task6:
    PATH_TO_ARCHIVE = os.path.abspath(__file__).replace("Task5.py", "voina-i-mir.zip")
    ALPHABET = 'qazwsxedcrfvtgbyhnujmikolp'

    def count_letters_in_text(self, text):
        result = {}
        for letter in text:
            for char in self.ALPHABET:
                if(char == letter or char.upper() == letter):
                    if result.get(letter):
                        result[char] += 1
                    else:
                        result[char] = 1
        return result

    def read_files_from_archive(self):
        with ZipFile(self.PATH_TO_ARCHIVE, "r") as myzip:
            for file_in_archive in myzip.namelist():
                with myzip.open(file_in_archive, 'r') as file:
                    result = self.count_letters_in_text(file.read())
        result = dict(sorted(result.items(), lambda item : item, reverse=True))
        return result
    
    def print_dict(self, dictionary):
        for key in dictionary.keys():
            print(f"{key} : {dictionary[key]}")
    
    def main(self):
        letters_amount = self.read_files_from_archive()
        self.print_dict(letters_amount)