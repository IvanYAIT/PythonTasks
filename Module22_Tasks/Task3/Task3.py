import os
from services.user_input import call_until_valid_input

class Task3:
    @call_until_valid_input
    def get_user_path():
        user_path = input("Пожалуйста, введите путь до директории: ")

        if(not os.path.isdir(user_path)):
            raise ValueError("Такой директории нет")
        
        return user_path
    
    def count_files_in_folder(path):
        result = 0
        for file in os.listdir(path):
            if(os.path.isfile(os.path.join(path, file))):
                result += 1
        return result

    def count_subfolders_in_folder(path):
        result = 0
        for file in os.listdir(path):
            if(os.path.isdir(os.path.join(path, file))):
                result += 1
        return result
    
    def count_folder_size(path):
        result = 0.0
        for file in os.listdir(path):
            result += (os.path.getsize(os.path.join(path, file)) / 1024)
        return result
    
    @classmethod
    def main(cls):
        path = cls.get_user_path()
        files_amount = cls.count_files_in_folder(path)
        subfolders_amount = cls.count_subfolders_in_folder(path)
        folder_size = cls.count_folder_size(path)
        print(f"Размер каталога (в Кб): {folder_size}\n", 
              f"Количество подкаталогов: {subfolders_amount}\n",
              f"Количество файлов: {files_amount}")