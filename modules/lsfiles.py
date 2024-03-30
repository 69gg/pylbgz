import os

def lsfiles(file_dir: str):
    '''
    lsfile("要列举的文件夹路径")
    '''
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list