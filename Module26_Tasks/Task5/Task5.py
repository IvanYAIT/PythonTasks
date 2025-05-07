class Task5:
    def get_errors(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                if line.lower().find('error ') > 0 or line.lower().startswith('error'):
                    yield line
                    