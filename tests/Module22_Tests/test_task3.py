from Module22_Tasks.Task3.Task3 import Task3

def test_count_files_in_folder():
    path = "C:\\Users\\user\\Downloads"
    assert Task3.count_files_in_folder(path) == 5

def test_count_subfolders_in_folder():
    path = "C:\\Users\\user\\Downloads"
    assert Task3.count_subfolders_in_folder(path) == 2

def test_count_folder_size():
    path = "C:\\Users\\user\\Downloads"
    assert Task3.count_folder_size(path) == 680620.994140625