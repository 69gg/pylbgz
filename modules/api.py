from flask import Flask, request, jsonify
import sys
sys.dont_write_bytecode = True
#禁用pyc

from modules.compress import *
from modules.decompress import *
from modules.lsfiles import *

app = Flask(__name__)

@app.route('/compress', methods=['GET'])
def get_compress():
    files = request.args.getlist('files')
    path = request.args.get('path', 'NewFile.pylbgz')
    result = compress(files, path)
    return result

@app.route('/decompress', methods=['GET'])
def get_decompress():
    file = request.args.getlist('input')
    path = request.args.get('outputpath')
    result = decompress(file, path)
    return result

@app.route('/lsfiles', methods=['GET'])
def get_compress():
    path = request.args.get('path')
    result = lsfiles(path)
    return result

def api() -> None: 
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)

