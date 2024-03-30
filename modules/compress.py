import json

def compress(files: list, path = "NewFile.pylbgz") -> json:
    '''
    compress("文件列表", "输出压缩文件路径")
    '''
    with open(path, 'wb') as pylbgzf:
        pylbgzf.write(b"pylbgz_file\n")
    for file in files:
        try:
            with open(file, 'rb') as f:
                content = f.read()
            with open(path, 'ab') as pybgzf:
                pybgzf.write(b"START PYLBGZ FILE\n" + file.encode('utf-8') + b"START")
                pybgzf.write(content)
                pybgzf.write(b"END PYLBGZ FILE\n" + file.encode('utf-8') + b"END")
        except FileNotFoundError:
            data = {"state": "Error", 
                    "Error": 
                        {
                        "Msg": f"The file '{file}' cannot be found by us.", "Error": "FileNotFound"
                        }
                    }
            return json.dumps(data)
    return json.dumps({"state": "Success", "Msg": "Files compressed successfully."})