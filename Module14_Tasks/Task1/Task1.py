import sys, platform, os # Добавил импорты

class Task1:
    
    def main():
        FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "os_info.txt") # Добавил константу 

        info = 'OS info is \n{}\n\nPython version is {} {}'.format(
            platform.uname(),
            sys.version,
            platform.architecture(),
        )
        print(info)

        # Заменил путь до файла константой
        # Изменил тип чтения файла на Запись
        # Поменял название переменной с fl на file
        with open(FILE_PATH, "w+", encoding='utf8') as file:  
            file.write(info)