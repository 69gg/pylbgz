根据提供的信息，以下是README.md文件的内容：

# Pylbgz
Pylbgz是一个小型的的Python项目，用于打包和复原文件。它基于Python语言，并配套了PylbgzShell工具来方便的进行用户操作。
PylbgzShell是一个简单的Python Shell工具，用于压缩和解压文件。用户可以通过命令行输入指令来进行文件的压缩和解压操作。

## 使用方法-PylbgzShell

请先运行`PylbgzShell.py`进入用户命令行控制界面。

### 压缩文件

```PylbgzShell
compress file1.txt,file2.txt output compressed_folder
```

### 解压文件

```PylbgzShell
decompress compressed_file.pylbgz output_folder
```

### 列出文件

```PylbgzShell
lsfiles path_to_directory
```

### 创建文件夹

```PylbgzShell
mkdir new_folder
```

### 退出PylbgzShell

```PylbgzShell
exit
```

## 使用方法-Pylbgz Modules

查看`main.py`来获取引入库的方法。

方法：
    1. 压缩文件：`compress(file_paths, output_file_path)`
    2. 解压文件：`decompress(file_path, output_files_path)`
    3. 列出文件：`lsfiles(directory_path)`