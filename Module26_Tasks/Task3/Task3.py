import os

class Task3:
    def count_lines_in_py_file(self, path):
        result = 0
        for root, dir, files in os.walk(path):
            for name in files:
                if name[-3:] != '.py':
                    continue

                path_to_file = os.path.join(root, name)
                with open(path_to_file, 'r', encoding='utf-8') as file:
                    for line in file.readlines():
                        if len(line) > 2 and not line.startswith('#'):
                            result += 1
        return result