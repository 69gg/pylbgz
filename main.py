import sys
sys.dont_write_bytecode = True
#禁用pyc

from modules.compress import compress
from modules.decompress import decompress
from modules.lsfiles import lsfiles
from api import api

# to do
api()