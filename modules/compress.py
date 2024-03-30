import json

def compress(files: list, path = "./NewFile.pylbgz") -> json:
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
            return json.dumps({"state": "Error", "Error": {"Msg": "The file cannot be found by us.", "Error": "FileNotFound"}})
