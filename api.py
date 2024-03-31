from flask import Flask, request

import sys
sys.dont_write_bytecode = True
#禁用pyc

from modules.compress import compress as c
from modules.decompress import decompress as dc
from modules.lsfiles import lsfiles as ls

app = Flask(__name__)

@app.route('/compress', methods=['GET'])
def compress():
    files = request.args.get('files')
    path = request.args.get('path')
    files = files.replace("'", "").split(',')
    if path is None:
        result = c(files)
        return result
    else:
        result = c(files, path)
        return result

@app.route('/decompress', methods=['GET'])
def decompress():
    file = request.args.get('file')
    path = request.args.get('path')
    if file is None:
        data = {'status': 'error', 'message': 'No input path selected.'}
        return data
    elif path is None:
        data = {'status': 'error', 'message': 'No output path selected.'}
        return data
    else:
        result = dc(file, path)
        return result

@app.route('/lsfiles', methods=['GET'])
def lsfiles():
    path = request.args.get('path')
    if path is None:
        data = {'status': 'error', 'message': 'No path selected.'}
        return data
    else:
        result = ls(path)
        result = result[1:-1]
        return result

def api(port: int = 5000) -> None: 
    app.run(debug=True, port=port)

if __name__ == '__main__':
    api()
