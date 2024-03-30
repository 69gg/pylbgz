import os
import re
import sys

from modules.compress import *
from modules.decompress import *
from modules.lsfiles import *

while True:
    try:
        cwd = os.getcwd()

        content = input(f"PylbgzShell {cwd} $ ")
    
        compress_match = re.match(r'^compress (.+) output (.+)', content)
        decompress_match = re.match(r'^decompress (.+) output (.+)', content)
        ls_match = re.match(r'^ls (.+)', content)
    
        if compress_match:
            files = compress_match.group(1).split(',')
            output_path = compress_match.group(2)
            result = compress(files, output_path)
            print(result)
    
        elif decompress_match:
            input_path = decompress_match.group(1)
            output_path = decompress_match.group(2)
            result = decompress(input_path, output_path)
            print(result)

        elif ls_match:
            path = content[3:]
            result = lsfiles(path)
            print(result)

        elif content == "exit":
            sys.exit()

        elif content == "":
            pass

        else:
            print("Invalid command. Please try again.")

    except KeyboardInterrupt:
        print("\nUse 'exit' to exit.")