import json

def decompress(path: str, output_path: str) -> json:
    try:
        with open(path, 'rb') as pylbgzf:
            content = pylbgzf.read()
        
        if content.startswith(b"pylbgz_file\n"):
            files_data = content.split(b"START PYLBGZ FILE\n")[1:]
            for file_data in files_data:
                file_name_end_index = file_data.find(b"START")
                file_name = file_data[:file_name_end_index].decode()
                file_content = file_data[file_name_end_index + 5:-18]
                
                with open(output_path + file_name, 'wb') as f:
                    f.write(file_content)
                    
                
            return json.dumps({"state": "Success", "Msg": "Files decompressed successfully."})
        else:
            return json.dumps({"state": "Error", "Error": {"Msg": "Invalid compressed file format.", "Error": "InvalidFormat"}})
    
    except FileNotFoundError:
        return json.dumps({"state": "Error", "Error": {"Msg": "The compressed file cannot be found.", "Error": "FileNotFound"}})