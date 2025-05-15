class Task1:
    def open_file(self, path):
        try:
            with open(path, '+a', encoding='utf-8') as file:
                file.write(input('Что записать в файл: '))
        except:
            return
