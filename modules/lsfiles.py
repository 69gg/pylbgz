import os

def lsfiles(file_dir: str):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list