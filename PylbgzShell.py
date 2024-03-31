import os
import re

import sys
sys.dont_write_bytecode = True
#禁用pyc

from modules.compress import *
from modules.decompress import *
from modules.lsfiles import *

while True:
    try:
        cwd = os.getcwd()

        content = input(f"PylbgzShell {cwd} $ ")
    
        compress_match = re.match(r'^compress (.+) output (.+)', content)
        decompress_match = re.match(r'^decompress (.+) output (.+)', content)
        compress_match2 = re.match(r'^compress (.+)', content)
        lsfiles_match = re.match(r'^lsfiles (.+)', content)
        mkdir_match = re.match(r'^mkdir (.+)', content)
    
        if compress_match:
            files = compress_match.group(1).split(',')
            output_path = compress_match.group(2)
            result = compress(files, output_path)
            print(result)

        if compress_match2:
            files = compress_match2.group(1).split(',')
            result = compress(files)
            print(result)
    
        elif decompress_match:
            input_path = decompress_match.group(1)
            output_path = decompress_match.group(2)
            result = decompress(input_path, output_path)
            print(result)

        elif lsfiles_match:
            path = content[8:]
            result = lsfiles(path)
            print(result)
        
        elif content == "ls":
            print(os.listdir())

        elif content == "exit":
            sys.exit()

        elif content == "":
            pass

        elif mkdir_match:
            path = mkdir_match.group(1)
            os.mkdir(path)

        else:
            print("Invalid command. Please try again.")

    except KeyboardInterrupt:
        print("\nUse 'exit' to exit.")