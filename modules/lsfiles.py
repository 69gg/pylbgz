import os

#遍历目标文件夹所有文件，输出完整路径
def lsfiles(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list