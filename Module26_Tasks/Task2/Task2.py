import os

class Task2:
    def gen_files_path(self, path):
        for root, dir, files in os.walk(path):
            for name in files:
                print(os.path.join(root, name))