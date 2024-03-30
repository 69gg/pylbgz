import json
import os

def decompress(input_path: str, output_path: str) -> json:
    '''
    decompress("输入压缩文件路径", "输出文件夹路径")
    '''
    try:
        with open(input_path, 'rb') as pylbgzf:
            content = pylbgzf.read()
        
        if content.startswith(b"pylbgz_file\n"):
            if not os.path.exists(output_path):
                os.makedirs(output_path)  # 创建输出路径
            
            files_data = content.split(b"START PYLBGZ FILE\n")[1:]
            for file_data in files_data:
                file_name_end_index = file_data.find(b"START")
                file_name = file_data[:file_name_end_index].decode()
                file_content = file_data[file_name_end_index + 5:-18]
                
                abs_file_path = os.path.join(output_path, file_name)  # 使用绝对路径
                
                # 创建文件夹（如果需要）
                folder_path = os.path.dirname(abs_file_path)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                with open(abs_file_path, 'wb') as f:
                    f.write(file_content)
                    
            return json.dumps({"state": "Success", "Msg": "Files decompressed successfully."})
        else:
            return json.dumps({"state": "Error", "Error": {"Msg": "Invalid compressed file format.", "Error": "InvalidFormat"}})
    
    except FileNotFoundError as e:
        data = {
            "state": "Error", 
            "Error": 
                {
                    "Msg": f"Error: {str(e)}", "Error": "FileNotFound"
                }
        }
        return json.dumps(data)