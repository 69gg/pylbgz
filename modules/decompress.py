import json
import os

def decompress(path: str, output_path: str) -> json:
    if output_path[-1] != '/' or output_path[-1] != '\\':
        output_path += '/'
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
        data = {
            "state": "Error", 
            "Error": 
                    {
                        "Msg": f"The compressed file '{path}' cannot be found.", "Error": "FileNotFound"
                    }
                }
        return json.dumps(data)