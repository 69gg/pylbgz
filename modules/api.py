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
    files = request.args.getlist('files')
    path = request.args.get('path', 'NewFile.pylbgz')
    result = c(files, path)
    return result

@app.route('/decompress', methods=['GET'])
def decompress():
    file = request.args.getlist('input')
    path = request.args.get('outputpath')
    result = dc(file, path)
    return result

@app.route('/lsfiles', methods=['GET'])
def lsfiles():
    path = request.args.get('path')
    result = ls(path)
    return result

def api(port: int = 5000) -> None: 
    app.run(debug=True, port=port)


if __name__ == '__main__':
    app.run(debug=True)

