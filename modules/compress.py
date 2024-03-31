import json

def compress(files: list, path = "NewFile.pylbgz") -> dict:
    with open(path, 'w') as pylbgzf:
        pylbgzf.write("pylbgz_file")
    for file in files:
        try:
            with open(file, 'rb') as f:
                content = f.read()
            with open(path, 'a') as pybgzf:
                pybgzf.write("START PYLBGZ FILE" + file + "START")
            with open(path, 'ab') as pybgzf:
                pybgzf.write(content)
            with open(path, 'a') as pybgzf:
                pybgzf.write("END PYLBGZ FILE" + file + "END")
        except FileNotFoundError:
            data = {"state": "Error", 
                    "Error": {
                        "Msg": f"The file '{file}' cannot be found by us.", "Error": "FileNotFound",
                        "result": f"files {files}, path {path}"
                    }
            }
            return data
    return {"state": "Success", "Msg": "Files compressed successfully."}